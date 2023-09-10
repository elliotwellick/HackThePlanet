import sys
import requests
import json

if len(sys.argv) != 2:
    print("Usage: python hacktheplanet.py <IP_address>")
    sys.exit(1)

ip_address = sys.argv[1]
url = f'https://internetdb.shodan.io/{ip_address}'

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  

        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
