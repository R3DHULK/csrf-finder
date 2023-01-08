import requests

# banner
print('''\033[93m
   ___ ___ ___ ___   ___ _         _         
  / __/ __| _ \ __| | __(_)_ _  __| |___ _ _ 
 | (__\__ \   / _|  | _|| | ' \/ _` / -_) '_|
  \___|___/_|_\_|   |_| |_|_||_\__,_\___|_|  
   
   GIthub Page: https://github.com/R3DHULK
   coded by R3DHULK
''')

# Send a GET request to the web application
response = requests.get(input("\033[92m [*] Enter URL: "))

# Check the response for any indicators of a CSRF vulnerability
if response.status_code == 200:
    if "csrf_token" in response.text:
        print("\033[91m [-] CSRF Protection is Present\033[91m")
    else:
        print("\033[94m [+] No CSRF Protection Found\033[94m")
else:
    print("Error:", response.status_code)
