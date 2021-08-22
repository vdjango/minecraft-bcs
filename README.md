# Minecraft 协议

## 协议版本 1.16.5

> 十六进制

### 客户端操作-多人游戏

｜ 操作 | 客户端 | 服务端 |
|  ---- | ---- | ---- |
｜ 刷新 | `\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00` ｜ |
｜ 加入服务器 | `\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x02\x07\x00\x05junsi` ｜ |

### 

* **刷新**
```shell
# 客户端
\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00
密 16 00 f2 05 0f 127.0.0.1 00 FML2 00 \t  fc 01 01 00
解 SYN NUL [F2] ENQ SI 127.0.0.1 NUL FML2 NUL HT [FC] SOH SOH NUL

# 服务端
\x8f:\x00\x8c:{"description":{"text":"A Minecraft Server"},"players":...
密 8f 3a 00 8c 3a 解 [8F] : NUL [8C] : {"description":{"text":"A Minecraft Server"},"players":...

# 服务端发送数据
{
    "description": {
        "text": "A Minecraft Server"
    },
    "players": {
        "max": 20,
        "online": 0
    },
    "version": {
        "name": "Mohist 1.16.5",
        "protocol": 754
    },
    "forgeData": {
        "channels": [
            {
                "res": "valkyrielib:main",
                "version": "1.0.0",
                "required": false
            },
            {
                "res": "projecte:main_channel",
                "version": "1",
                "required": false
            },
            {
                "res": "firstaid:channel",
                "version": "3.0",
                "required": false
            },
            {
                "res": "jei:channel",
                "version": "1.0.0",
                "required": true
            },
            // ..
        ],
        "mods": [
            {
                "modId": "botaniaadditions",
                "modmarker": "1.0.4"
            },
            {
                "modId": "ftbessentials",
                "modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"
            },
            {
                "modId": "trashslot",
                "modmarker": "12.2.1"
            },
            {
                "modId": "aiotbotania",
                "modmarker": "1.8.0"
            },
            {
                "modId": "ftblibrary",
                "modmarker": "1605.3.1-build.58"
            }
            // ...
        ],
        "fmlNetworkVersion": 2,
        "truncated": false
    }
}'

```

* **加入服务器客户端发送数据**
```text
\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x02\x07\x00\x05junsi
```

* **服务器回传数据**

```text
接受到客户端数据 b'\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x02\x07\x00\x05junsi'
```