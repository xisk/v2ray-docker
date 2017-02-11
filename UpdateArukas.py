# -*- coding: utf-8 -*-

import json
import os
import requests
import re

config_file_path = "/etc/v2ray/config.json"

arukas_user = [
    {
        "email": "FOO@BAR.COM",
        "password": "PASSWORD"
    }
]

node_vmess = {
    "address": "0.0.0.0",
    "port": 0,
    "users": [
        {
            "id": "67a7ac7f-3656-a5f3-3434-a3faaa744770",
            "alterId": 1
        }
    ]
}

ports_used = [
    {'number': 10010, 'protocol': 'udp'}
]

config = {
    "log": {
        "error": "/var/log/v2ray/error.log",
        "loglevel": "warning"
    },
    "inbound": {
        "port": 1080,
        "listen": "127.0.0.1",
        "protocol": "socks",
        "settings": {
            "auth": "noauth",
            "udp": False
        }
    },
    "outbound": {
        "protocol": "vmess",
        "settings": {
            "vnext": []
        }
    },
    "outboundDetour": [
        {
            "protocol": "freedom",
            "settings": {},
            "tag": "direct"
        }
    ],
    "dns": {
        "servers": [
            "8.8.8.8",
            "8.8.4.4",

            "208.67.222.222",
            "208.67.220.220",

            "199.85.126.30",
            "199.85.127.30",

            "156.154.70.1",
            "156.154.71.1",

            "localhost"
        ]
    },
    "routing": {
        "strategy": "rules",
        "settings": {
            "domainStrategy": "IPIfNonMatch",
            "rules": [
                {
                    "type": "field",
                    "ip": [
                        "0.0.0.0/8",
                        "10.0.0.0/8",
                        "100.64.0.0/10",
                        "127.0.0.0/8",
                        "169.254.0.0/16",
                        "172.16.0.0/12",
                        "192.0.0.0/24",
                        "192.0.2.0/24",
                        "192.168.0.0/16",
                        "198.18.0.0/15",
                        "198.51.100.0/24",
                        "203.0.113.0/24",
                        "::1/128",
                        "fc00::/7",
                        "fe80::/10"
                    ],
                    "outboundTag": "direct"
                },
                {
                    "type": "chinaip",
                    "outboundTag": "direct"
                },
                {
                    "type": "chinasites",
                    "outboundTag": "direct"
                }
            ]
        }
    },
    "transport": {
        "kcpSettings": {
            "uplinkCapacity": 50,
            "downlinkCapacity": 50
        }
    }
}


def main():
    url_login = "https://app.arukas.io/api/login"
    url_container = "https://app.arukas.io/api/containers"

    for user_info in arukas_user:
        try:
            # 登录
            login_result = requests.post(url_login, data=user_info, timeout=5)
            assert 'OK' == login_result.json()['message']

            # 获取Container信息
            header = {
                'Cookie': ""
            }
            for cookie in login_result.cookies.items():
                header['Cookie'] += cookie[0] + "=" + cookie[1] + ";"
            container_result = requests.get(url_container, headers=header, timeout=5)
            assert 200 == container_result.status_code
            container_detail = container_result.json()

            # 解析得到节点信息
            for container in container_detail["data"]:
                for port_aim in ports_used:
                    try:
                        ith = container["attributes"]["ports"].index(port_aim)
                        node_select = container["attributes"]["port_mappings"][0][ith]

                        ip = re.findall(r'\d{1,3}-\d{1,3}-\d{1,3}-\d{1,3}', node_select['host'])[0].replace('-', '.')
                        port = node_select['service_port']

                        node = node_vmess.copy()
                        node["address"] = ip
                        node["port"] = port

                        config["outbound"]["settings"]["vnext"].append(node)
                    except:
                        pass
        except Exception as e:
            print(e)

    # 写入配置文件
    with open(config_file_path, mode='w') as f:
        print(json.dumps(config, sort_keys=True, indent=4), file=f)

    # 重启V2Ray
    os.system("service v2ray restart")


if "__main__" == __name__:
    main()
    print("Done")
