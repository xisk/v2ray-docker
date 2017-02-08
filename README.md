# v2ray-docker

## Introduction

An out-of-the-box V2Ray Docker

## Custom Configuration

To use your own `config.json`, you should encode the config file with __base64__, and set the docker ENV `ENV_V2RAYCONFIG`.

## Ports

| Port | Type | function |
| :--: | :--: | :--: |
| 10010 | UDP | V2Ray |
| 10086 | TCP | ShadowSocks |
