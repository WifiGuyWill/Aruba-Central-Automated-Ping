# Aruba Central AP Ping Test Script
Script to automate the Ping test on APs in Aruba Central

```
% python3 main.py
--- Starting ---
CNKDKSM0RQ round-trip min/avg/max = 4.9/5.4/6.1 ms
CNKDKSM0SC round-trip min/avg/max = 4.7/5.0/5.3 ms
--- Finished ---
NOTE: Output saved to ap_data.txt
```

Download the repo, make sure Python is installed.
Edit creds.py and enter the credentials for Aruba Central.
Then execute the script 'python3 main.py'

The script will first generate a valid API key, then create a list of every active AP in Central. It will then run the ping command to the host defined in the script. The output will be shown on the screen as the script executes and written to a file called 'ap_data.txt'.

>>Need to add additional varificaion for ping command completion before executing GET export of the results.

Please feel free to modify or provide any comments or feedback.

Thank you - Will Smith
will@wifi-guys.com