# Aruba Central AP Ping Test Script
Script to automate the Ping test on APs in Aruba Central

```
% python3 main.py apple.com
Ping Test Results to apple.com
--- Starting ---
CNKDKSM0RQ round-trip min/avg/max = 4.8/5.8/8.7 ms
CNKDKSM0SC round-trip min/avg/max = 4.7/5.1/5.8 ms
--- Finished ---
NOTE: Output saved to ap_data.txt
```

Download the repo, make sure Python is installed.
Edit creds.py and enter the credentials for Aruba Central.
Then execute the script with the host info 'python3 main.py apple.com'

The script will first generate a valid API key, then create a list of every active AP in Central. It will then run the ping command to the host defined in the script. The output will be shown on the screen as the script executes and written to a file called 'ap_data.txt'.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com
