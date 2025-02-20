import yaml
import requests
import json
from requests.auth import HTTPBasicAuth

# Load router configuration from YAML file
with open("labquestions.yml", "r") as file:
    config = yaml.safe_load(file)

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = 'http://{0}/restconf/api/running/'.format(HOST)

# Function to configure interface via RESTCONF
def configure_interface(router_ip, interface, ip_address):
    url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface={interface}"
    
    # Interface payload
    payload = {
        "ietf-interfaces:interface": {
            "name": interface,
            "enabled": True,
            "type": "iana-if-type:ethernetCsmacd",
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_address.split('/')[0],
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }
    
    try:
        # Send RESTCONF PUT request
        response = requests.put(url, auth=HTTPBasicAuth(USERNAME, PASSWORD),
                                headers=HEADERS, json=payload, verify=False)
        
        if response.status_code in [200, 201, 204]:
            print(f"Successfully configured {interface} on {router_ip} with IP {ip_address}")
        else:
            print(f"Failed to configure {interface} on {router_ip}. Error: {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Connection error to {router_ip}: {e}")

# Loop through each router in the YAML file and configure interfaces
for router, details in config["routers"].items():
    router_ip = details["management_ip"]
    for interface, ip_address in details["interfaces"].items():
        configure_interface(router_ip, interface, ip_address)
