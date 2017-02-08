#!/bin/bash

# Install
bash <(curl -L -s https://install.direct/go.sh)

# ENV2Config
if [ -n "$ENV_V2RAYCONFIG" ]; then
    echo $ENV_V2RAYCONFIG | base64 -d > /etc/v2ray/config.json
fi

# Run
/usr/bin/v2ray/v2ray -config /etc/v2ray/config.json
