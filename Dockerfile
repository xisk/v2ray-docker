FROM ubuntu
MAINTAINER "jinyu121" <jinyu121@126.com>

# Basic environment setting
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apt update \
    && apt upgrade -y \
    && apt install git curl unzip wget -y

# Port for v2ray
EXPOSE 10010

# Port for ShadowSocks
EXPOSE 10086

# Copy configuration file
ADD config.json /etc/v2ray/config.json
ADD run.sh /etc/v2ray/run.sh

# Have fun
ENTRYPOINT ["/bin/bash", "/usr/bin/v2ray/run.sh"]
