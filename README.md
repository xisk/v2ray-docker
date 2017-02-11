# v2ray-docker

## Introduction

An out-of-the-box V2Ray Docker.

## Configuration

### Server

To use your own `config.json`, you should encode the config file with __base64__, and set the encoded string to docker ENV `ENV_V2RAYCONFIG`.

### Client

You can use `tools/UpdateArukas.py` to update nodes info.

We use dict `config` in `tools/UpdateArukas.py` as the model of `config.json`.

## Ports

| Port | Type | Function |
| :--: | :--: | :--: |
| 10010 | UDP | V2Ray |
| 10086 | TCP | ShadowSocks |
