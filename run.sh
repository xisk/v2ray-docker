#!/bin/bash

bash <(curl -L -s https://install.direct/go.sh)

/usr/bin/v2ray/v2ray -config /etc/v2ray/config.json
