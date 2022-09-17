#!/usr/bin/python3
#(c) 2022 Will Smith

#First populate creds.py with Central info + API keys
#Run this script to generate a inventory list of all active AP serial numbers
#Then each AP will execute a ping to the defined host with the min/max/avg times
#Output will be shown on the screen and a file called ap_data.txt is also generated

from pycentral.base import ArubaCentralBase
import creds as creds
import time
import sys

host = str(sys.argv[1])
#host = apple.com

central_info = creds.central_info
central = ArubaCentralBase(central_info=central_info, ssl_verify=True)

#This function will generate a list of the serial numbers for all active APs
def inventory():
    offset = 0
    f = open("temp/serial.txt", "w")
    while True:
        inventory_response = central.command(apiMethod="GET", apiPath="/monitoring/v2/aps", apiParams={"limit": 1000, "offset": offset})
        for aps in inventory_response["aps"]:
            f.write(aps["serial"] + "\n")
        offset = offset + 1000
        if int(inventory_response['count']) == 0:
            break

#This function will run the troubleshooting PING command
def ap_ping():
    ap_data = open("ap_data.txt", "w")
    with open('temp/serial.txt') as f:
        for line in f:
            serial = line.strip()
            ap_ping_command = central.command(apiMethod="POST", apiPath="/troubleshooting/v1/devices/" + serial, apiData=
            {
            "device_type": "IAP",
            "commands": [
                {
                "command_id": 165,
                "arguments": [
                    {
                    "name": "Host",
                    "value": host
                    }
                ]
                }
            ]
            })
            ap_session_id = str(ap_ping_command["session_id"])
            time.sleep(7)
            ap_ping_response = central.command(apiMethod="GET", apiPath="/troubleshooting/v1/devices/" + serial + "/export?session_id=" + ap_session_id)
            try:
                if (ap_ping_response.get("code")) == 200 :
                    ap_ping_msg = ap_ping_response['msg']
                    for line in ap_ping_msg.splitlines()[::-1]:
                        if "round-trip" in line:
                            ping_output_line = line.strip()
                            print(serial + " " + ping_output_line)
                            ap_data.write(serial + " " + ping_output_line + "\n")
                else:
                    time.sleep(7)
                    ap_ping_response = central.command(apiMethod="GET", apiPath="/troubleshooting/v1/devices/" + serial + "/export?session_id=" + ap_session_id)
                    ap_ping_msg = ap_ping_response['msg']
                    for line in ap_ping_msg.splitlines()[::-1]:
                        if "round-trip" in line:
                            ping_output_line = line.strip()
                            print(serial + " " + ping_output_line)
                            ap_data.write(serial + " " + ping_output_line + "\n")
            except:
                pass


if __name__ == "__main__":
    print("--- Starting ---")
    inventory()
    ap_ping()
    print("--- Finished ---")
    print("NOTE: Output saved to ap_data.txt")
