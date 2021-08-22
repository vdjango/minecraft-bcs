# Minecraft 协议

## 协议版本 1.16.5

> 数据为十六进制数据流形式

### 已解析

 | 操作 | 文档 | 修订 |
 | ---- | ---- | ---- |
 | 刷新 | ～ | 2021-08-22 |
 | 加入服务器 | ～ | 2021-08-22 |

#### 刷新操作
* **客户端发送**

`\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00`

```shell
密 16 00 f2 05 0f 127.0.0.1 00 FML2 00 \t  fc 01 01 00
解 SYN NUL [F2] ENQ SI 127.0.0.1 NUL FML2 NUL HT [FC] SOH SOH NUL
```

* **服务端回传**

`\x8f:\x00\x8c:{"description":{"text":"A Minecraft Server"},"players":...`

```shell
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
            // ...
        ],
        "fmlNetworkVersion": 2,
        "truncated": false
    }
}'
```

* **客户端发送**

`\t\x01\x00\x00\x00\x00\x01\xf7\x11\xda`

```shell
密 09 01 00 00 00 00 01 f7 11 da
解 HT SOH NUL NUL NUL NUL SOH [f7] DC1 [da]
```

* **服务端回传**

`\t\x01\x00\x00\x00\x00\x01\xf7\x11\xda`

```shell
密 09 01 00 00 00 00 01 f7 11 da
解 HT SOH NUL NUL NUL NUL SOH [f7] DC1 [da]
```

#### 加入服务器操作


* **客户端发送**

`\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x02\x07\x00\x05junsi`

```shell
# 玩家名称: junsi 
# 服务器地址: 127.0.0.1
密 16 00 f2 05 0f 00 127.0.0.1 FML2 00 09 fc 02 07 00 05 junsi
解 SYN NUL [F2] ENQ SI NUL 127.0.0.1 FML2 NUL HT [FC] STX BEL NUL ENQ junsi
```

* **服务器回传数据 （一共N组数据）**

```shell
# 
```

```shell
# 
```

```shell
# 
```
