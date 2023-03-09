import json
import os
import time
import subprocess

RETRY_COUNT=3

config_working = """
{
  "inbounds": [
    {
      "port": 1088, // Listening port
      "protocol": "socks", // Incoming protocol is SOCKS 5
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      },
      "settings": {
        "auth": "noauth"  
      }
    }
  ],
  "outbounds": [
     {
        "protocol": "{protocol}",
        "settings": {
            "vnext": [
                {
                    "address": "{server_name}", 
                    "port": {port_number},
                    "users": [
                        {
                            "id": "{uuid}",
                            "encryption": "none"
                        }
                    ]
                }
            ]
        },
        "streamSettings": {
          "network": "ws",
          "security": "none",
          "wsSettings": {
            "acceptProxyProtocol": false,
            "path": "{path}",
            "headers": {
              "Host": "{host}"
            }
          }
        }
    }
  ]
}
"""

server_info = {
    "name": "mahsa2355eyh",
    "address": "185.148.107.12",
    "port": 80,
    "host": "m235.saqezonline.uk",
    "protocol": "vmess",
    "uuid": "3a1cb91b-215e-47ba-97d4-e8a70b30bc2d",
    "path": "/rhealth_check_user_mahsa2355eyh"
} 

server_names = [
    "104.22.59.173",
    "whatruns.com",
    "avval.ir",
    "mediaad.org",
    "opizo.me",
    "researchgate.net",
    "it-tech.com.au",
    "bamilo.com",
    "azaronline.com",
    "metrix.ir",
    "tapsell.ir",
    "tgju.org",
    "cdnjs.com",
    "188.42.88.227",
    "188.42.89.174",
    "203.23.103.248",
    "154.84.175.90",
    "195.137.167.16",
    "203.29.53.252",
    "185.201.139.68",
    "191.101.251.144",
    "188.42.88.252",
    "170.114.46.36",
    "188.42.89.1",
    "188.42.88.218",
    "188.42.88.252",
    "188.42.88.227",
    "188.42.88.242",
    "188.42.88.247",
    "188.42.88.237",
    "203.32.120.241",
    "141.193.213.22",
    "141.193.213.16",
    "188.42.88.238",
    "188.42.89.24",
    "188.42.89.4",
    "108.165.216.227",
    "147.185.161.244",
    "199.181.197.13",
    "45.142.120.30",
    "188.42.89.124",
    "188.42.89.126",
    "188.42.89.136",
    "203.34.28.158",
    "188.42.89.19",
    "108.165.216.219",
    "147.185.161.243",
    "203.32.121.151",
    "203.32.121.156",
    "199.181.197.26",
    "195.245.221.42",
    "203.29.53.252",
    "203.30.191.40",
    "45.133.247.24",
    "170.114.46.36",
    "185.176.26.19",
    "160.153.0.67",
    "108.165.216.213",
    "147.185.161.212",
    "195.137.167.16",
    "203.24.102.177",
    "185.221.160.12",
]

def average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)
    
hosts_avg = {}

for server_name in server_names:
    host = server_info["host"]
    config_str = config_working.replace(
        "{server_name}", server_name ).replace(
        "{port_number}", str(server_info["port"])).replace(
        "{uuid}", server_info["uuid"]).replace(
        "{protocol}", server_info["protocol"]).replace(
        "{host}", host).replace(
        "{path}", server_info["path"])

    with open("config.config", "w") as outfile:
        outfile.write(config_str)
    
    os.system("./v2ray/v2ray -config config.config > /dev/null 2>&1 &")

    time.sleep(1)

    results =[]
    print(f"testing {host}/{server_name}")
    for i in range(0, RETRY_COUNT): #try count
      successful = False
      try:
        cmd = "curl --max-time 10 --socks5 localhost:1088 -s -o /dev/null -w %{time_total} http://speedtest.ftp.otenet.gr/files/test1Mb.db"
        curl_output = subprocess.check_output(cmd,
                                          stderr=subprocess.STDOUT,
                                          shell=True)
        successful = True
        output_float = float(curl_output)
        results.append(output_float)
      except:
        print("An exception occurred")
      if not successful:
          print(f"failed try #{i+1}")

    avg = average(results)
    if len(results) > 0:
      print(f"Total time for {host} with {server_name} is {results}, average: {avg}")
    else:
      print(f"FAILED TO CONNECT TO {host}/{server_name}")
  
    hosts_avg[f"{server_name}/{host}"] = avg

    os.system("killall v2ray")


sorted_hosts_by_delay = sorted(hosts_avg.items(), key=lambda x:x[1])
print(sorted_hosts_by_delay)

ip_addresses = [x[0].split("/")[0] for x in sorted_hosts_by_delay if x[1]!=0][0:10]
print("Best 10 pops:")
print(",".join(ip_addresses))