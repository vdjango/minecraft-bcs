![minecraft](images/login.png)

# Minecraft 客户端/服务端协议解析（持续更新）
> 协议版本 1.16.5



## 协议解析

> 数据为十六进制数据流形式

### 已解析

 | 操作 | 文档 | 修订 |
 | ---- | ---- | ---- |
 | 刷新 | ～ | 2021-08-22 |
 | 加入服务器 | ～ | 2021-08-22 |

#### 刷新操作

* **客户端发送**

```shell
原 \x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00
密 16 00 f2 05 0f 127.0.0.1 00 FML2 00 \t  fc 01 01 00
解 SYN NUL [F2] ENQ SI 127.0.0.1 NUL FML2 NUL HT [FC] SOH SOH NUL
```

* **服务端回传**

```shell
原 \x8f:\x00\x8c:{"description":{"text":"A Minecraft Server"},"players":...
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

```shell
原 \t\x01\x00\x00\x00\x00\x01\xf7\x11\xda
密 09 01 00 00 00 00 01 f7 11 da
解 HT SOH NUL NUL NUL NUL SOH [f7] DC1 [da]
```

* **服务端回传**

```shell
原 \t\x01\x00\x00\x00\x00\x01\xf7\x11\xda
密 09 01 00 00 00 00 01 f7 11 da
解 HT SOH NUL NUL NUL NUL SOH [f7] DC1 [da]
```

#### 加入服务器操作


* **客户端发送**

```shell
# 玩家名称: junsi 
# 服务器地址: 127.0.0.1
原 \x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x02\x07\x00\x05junsi
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


## 基于协议的客户端/服务端操作
> 简单例子： 打开客户端多人游戏，会请求服务端服务器信息
>
> 创建 tcp socet 客户端监听25565端口，主动发送以下数据时会得到服务端的响应，具体格式如下
> 
> 请浏览 ping.json

* **Python3.6 代码示例**

> 需要安装 twisted 
> 
> `pip3.6 install twisted`

```python
from twisted.internet import reactor, protocol


class TSServProtocol(protocol.Protocol):
    c = None

    def connectionMade(self):
        '''
        当客户端连接的时候会执行该方法
        :return:
        '''
        self.c = self.transport.getPeer().host
        print("来自的{}链接:".format(self.c))

    def dataReceived(self, data):
        '''
        接收到客户端的数据
        :param data:
        :return:
        '''

        print("来自客户端:{}".format(data))
        # self.transport.write(data)
        pass


class MinecraftProtocol(protocol.Protocol):
    def send_message(self):
        send = b'\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00'
        print('发送数据 {}'.format(send))
        self.transport.write(send)

    def connectionMade(self):
        """
        创建连接时
        :return:
        """
        self.send_message()

    def dataReceived(self, data):
        """
        收到数据时
        :param data:
        :return:
        """
        print('收到数据', data)
        self.transport.loseConnection()  # 关闭连接
        print('done', )


class MinecraftProtocolFactory(protocol.ClientFactory):
    protocol = MinecraftProtocol
    clientConnctionLost = clientConnctionFailed = lambda self, connector, reason: reactor.stop()


if __name__ == '__main__':
    reactor.connectTCP('127.0.0.1', 25565, MinecraftProtocolFactory())
    reactor.run()

```


