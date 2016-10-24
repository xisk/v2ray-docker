FROM ubuntu
MAINTAINER "jinyu121" <jinyu121@126.com>

# Basic environment setting
RUN echo "Asia/Shanghai" > /etc/timezone
#RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN apt update -qq \
    && apt upgrade -y -qq \
    && apt install git curl unzip wget -y -q

# Setup V2Ray
RUN bash <(curl -L -s https://install.direct/go.sh)
RUN rm /usr/v2ray/config.json
ADD config.json /usr/v2ray/config.json
RUN service v2ray start

# Port for v2ray
EXPOSE 443

# Port for ShadowSocks
EXPOSE 80
