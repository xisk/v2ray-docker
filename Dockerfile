FROM ubuntu
MAINTAINER "jinyu121" <jinyu121@126.com>

# Basic environment setting
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apt update -qq \
    && apt upgrade -y -qq \
    && apt install git curl unzip wget -y -q

# Setup V2Ray
RUN curl -L -s https://raw.githubusercontent.com/v2ray/v2ray-core/master/release/install-release.sh | bash
RUN mv /etc/v2ray/config.json /etc/v2ray/config.json.bak
ADD config.json /usr/v2ray/config.json
RUN service v2ray start

# Port for v2ray
EXPOSE 443

# Port for ShadowSocks
EXPOSE 80
