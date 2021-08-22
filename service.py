# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name ：views
   Description :
   Author : cjh
   date ：2020-02-20
-------------------------------------------------
"""
import binascii
import struct
import time

from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientCreator, Factory


# from utils import hex2bin


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        '''
        当客户端连接的时候会执行该方法
        :return:
        '''
        clnt = self.clnt = self.transport.getPeer().host
        print(f"...来自的{clnt}链接:")

    def dataReceived(self, data):
        '''
        接收到客户端的数据
        :param data:
        :return:
        '''

        send = b'\x8f:\x00\x8c:{"description":{"text":"A Minecraft Server"},"players":{"max":20,"online":0},"version":{"name":"Mohist 1.16.5","protocol":754},"forgeData":{"channels":[{"res":"valkyrielib:main","version":"1.0.0","required":false},{"res":"projecte:main_channel","version":"1","required":false},{"res":"firstaid:channel","version":"3.0","required":false},{"res":"jei:channel","version":"1.0.0","required":true},{"res":"mantle:network","version":"1","required":false},{"res":"minecraft:unregister","version":"FML2","required":true},{"res":"mekanismmatter:mekanismmatter","version":"1","required":false},{"res":"champions:main","version":"1","required":false},{"res":"autoreglib:main","version":"1","required":false},{"res":"tconstruct:network","version":"1","required":false},{"res":"aiotbotania:netchannel","version":"1","required":false},{"res":"fastbench:channel","version":"1.1.0","required":true},{"res":"ccl:internal","version":"1","required":true},{"res":"journeymap:waypoint","version":"1","required":true},{"res":"journeymap:channel","version":"5.7.3","required":true},{"res":"immersiveengineering:main","version":"${version}","required":false},{"res":"mekanism:mekanism","version":"999.999.999","required":false},{"res":"botania:chan","version":"10","required":false},{"res":"fluxnetworks:main_network","version":"16fab291df61eb7a2c9705165ebbece6","required":false},{"res":"crafttweaker:main","version":"6.0.0","required":false},{"res":"journeymap:common","version":"5.7.3","required":true},{"res":"sereneseasons:main_channel","version":"0","required":false},{"res":"minecraft:register","version":"FML2","required":true},{"res":"envirocore:main","version":"1.0.0","required":false},{"res":"slashblade:main","version":"1","required":false},{"res":"minersadvantage:main_channel","version":"1.5","required":false},{"res":"toughasnails:main_channel","version":"0","required":false},{"res":"architectury:network","version":"1","required":true},{"res":"mekanismgenerators:mekanismgenerators","version":"999.999.999","required":false},{"res":"forge:split_11","version":"1.1","required":true},{"res":"curios:main","version":"1","required":false},{"res":"placebo:placebo","version":"1.0.0","required":true},{"res":"worldinfo:world_id","version":"1","required":true},{"res":"solcarrot:main","version":"1.0","required":false},{"res":"usefulbackpacks:curios","version":"1.16.3-1","required":false},{"res":"tombstone:tombstone_channel","version":"tombstone-6.4.7","required":false},{"res":"trashslot:network","version":"1.0","required":true},{"res":"torcherino:channel","version":"2","required":false},{"res":"patchouli:main","version":"1","required":false},{"res":"chisel:main","version":"1","required":false},{"res":"uteamcore:network","version":"1.16.5-1","required":false},{"res":"doggytalents:channel","version":"3","required":false},{"res":"waila:networking","version":"1.0.0","required":true},{"res":"ftbbackups:main","version":"1","required":true},{"res":"akashictome:main","version":"1","required":false},{"res":"inzhefopcore:inzhefopcore","version":"1","required":false},{"res":"forge:split","version":"1.0","required":true},{"res":"twilightforest:channel","version":"1","required":false},{"res":"refinedstorage:main_channel","version":"1","required":false}],"mods":[{"modId":"botaniaadditions","modmarker":"1.0.4"},{"modId":"ftbessentials","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"trashslot","modmarker":"12.2.1"},{"modId":"aiotbotania","modmarker":"1.8.0"},{"modId":"ftblibrary","modmarker":"1605.3.1-build.58"},{"modId":"jei","modmarker":"7.7.1.118"},{"modId":"slashblade","modmarker":"0.0.10"},{"modId":"doggytalents","modmarker":"2.0.1.10"},{"modId":"mekanism","modmarker":"10.0.21"},{"modId":"projecte","modmarker":"PE1.0.1B"},{"modId":"envirocore","modmarker":"1.16.5-3.0.9.1"},{"modId":"glassential","modmarker":"1.1.7"},{"modId":"passablefoliage","modmarker":"2.3.1"},{"modId":"envirotech","modmarker":"1.16.5-3.0.9.3"},{"modId":"controlling","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"ctm","modmarker":"MC1.16.1-1.1.2.6"},{"modId":"journeymap","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"placebo","modmarker":"4.5.0"},{"modId":"nofog","modmarker":"1.0.1"},{"modId":"botaniaendertransport","modmarker":"1.0"},{"modId":"sereneseasons","modmarker":"1.16.5-4.0.1.119"},{"modId":"mekanismmatter","modmarker":"1.19.0"},{"modId":"champions","modmarker":"1.16.5-2.0.1.7"},{"modId":"endercrop","modmarker":"1.16.5-1.6.0-beta"},{"modId":"uteamcore","modmarker":"3.2.1.196"},{"modId":"mekanismgenerators","modmarker":"10.0.21"},{"modId":"waila","modmarker":"1.10.11-B78_1.16.2"},{"modId":"jeitweaker","modmarker":"1.0.1.34"},{"modId":"fpsreducer","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"crafttweaker","modmarker":"7.1.0.371"},{"modId":"stevekungs_lib","modmarker":"4.1.5"},{"modId":"akashictome","modmarker":"1.4-16"},{"modId":"firstaid","modmarker":"1.9.6"},{"modId":"ftbteams","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"ftbchunks","modmarker":"1605.3.1-build.41"},{"modId":"forge","modmarker":"ANY"},{"modId":"inzhefopcore","modmarker":"1.0.0"},{"modId":"twilightforest","modmarker":"NONE"},{"modId":"refinedstorage","modmarker":"1.9.15"},{"modId":"minersadvantage","modmarker":"1.16.5-1.9.1.180"},{"modId":"minecraft","modmarker":"1.16.5"},{"modId":"tconstruct","modmarker":"3.1.1.252"},{"modId":"usefulbackpacks","modmarker":"1.12.1.90"},{"modId":"immersiveengineering","modmarker":"1.16.5-5.0.2-137"},{"modId":"mekanismadditions","modmarker":"10.0.21"},{"modId":"valkyrielib","modmarker":"1.16.5-3.0.9.2"},{"modId":"ftbranks","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"chunkanimator","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"toughnessbar","modmarker":"6.1"},{"modId":"backstab","modmarker":"1.1.1"},{"modId":"botania","modmarker":"1.16.5-419"},{"modId":"curios","modmarker":"1.16.5-4.0.5.2"},{"modId":"patchouli","modmarker":"1.16.4-53.1"},{"modId":"mantle","modmarker":"1.6.115"},{"modId":"ftbbackups","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"fastbench","modmarker":"4.5.1"},{"modId":"autoreglib","modmarker":"1.6-49"},{"modId":"fluxnetworks","modmarker":"6.1.7.12"},{"modId":"torcherino","modmarker":"14.0.0"},{"modId":"toughasnails","modmarker":"1.16.5-4.0.1.15"},{"modId":"ftbultimine","modmarker":"1605.3.0-build.25"},{"modId":"tombstone","modmarker":"6.4.7"},{"modId":"mekanismtools","modmarker":"10.0.21"},{"modId":"fastfurnace","modmarker":"4.4.0"},{"modId":"architectury","modmarker":"1.20.29"},{"modId":"chisel","modmarker":"MC1.16.5-2.0.1-alpha.4"},{"modId":"aiimprovements","modmarker":"0.3.0"},{"modId":"solcarrot","modmarker":"1.16.5-1.10.0"},{"modId":"cloth-config","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"},{"modId":"fastleafdecay","modmarker":"v25"},{"modId":"codechickenlib","modmarker":"4.0.2.429"},{"modId":"overloadedarmorbar","modmarker":"5.1.0"},{"modId":"wailaharvestability","modmarker":"OHNOES\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1\xf0\x9f\x98\xb1"}],"fmlNetworkVersion":2,"truncated":false}}'

        print(f"来自客户端:{data}")

        str_listx = []
        str_list = []
        c = binascii.hexlify(data)
        # for i in range(int(len(c) / 2)):
        #     bt_16 = c[2 * i:2 * (i + 1)]
        #     print('c', i, bt_16, chr(int(bt_16, 16)))
        #     str_list.append(chr(int(bt_16, 16)))
        #     str_listx.append(bt_16)

        # print(f"来自客户端:{''.join(str_list)}")
        # print(f"来自客户端:{str_listx}")
        # print(f"来自客户端:{hex2bin(binascii.hexlify(data))}")
        # print(f"来自客户端:{binascii.hexlify(data)}")

        # print(f"来自客户端:{msgpack.unpackb(data, encoding='utf')}")
        data = f"{time.ctime()}:来自服务器:你好"
        self.transport.write(send)


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            send = b'\x16\x00\xf2\x05\x0f127.0.0.1\x00FML2\x00\t\xfc\x01\x01\x00'
            print(f'...发送数据 {send}')
            # self.transport.write(msgpack.packb(data))
            self.transport.write(send)
            print('done')
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print('adasd', data)
        # print(msgpack.unpackb(data, encoding="utf8"))
        # self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnctionLost = clientConnctionFailed = lambda self, connector, reason: reactor.stop()


class Transfer(protocol.Protocol):
    def __init__(self):
        self.server = None
        pass

    def connectionMade(self):
        c = ClientCreator(reactor, Client_transfer)
        c.connectTCP("127.0.0.1", 25565).addCallback(self.set_protocol)
        self.transport.pauseProducing()

    def set_protocol(self, p):
        self.server = p
        p.set_protocol(self)

    def dataReceived(self, data):
        print('接受到客户端数据', data)
        self.server.transport.write(data)

    def connectionLost(self, reason):
        self.transport.loseConnection()
        self.server.transport.loseConnection()


class Client_transfer(protocol.Protocol):
    def __init__(self):
        self.server = None
        pass

    def set_protocol(self, p):
        self.server = p
        self.server.transport.resumeProducing()

    pass

    def dataReceived(self, data):
        print('接受到服务端数据', data)
        self.server.transport.write(data)

    pass


def run():
    # factory = protocol.Factory()
    # factory.protocol = TSServProtocol
    # print("....等待链接..")
    # # 使用reactor安装一个TCP监听器，检查服务请求。
    # # 当它接收到一个请求时,就会创建一个TSServProtocol实例来处理那个客户端的事务。
    # reactor.listenTCP(25565, factory)
    # reactor.run()

    reactor.connectTCP('127.0.0.1', 25565, TSClntFactory())
    reactor.run()


def run_server():
    # factory = protocol.Factory()
    # factory.protocol = TSServProtocol
    # print("....等待链接..")
    # # 使用reactor安装一个TCP监听器，检查服务请求。
    # # 当它接收到一个请求时,就会创建一个TSServProtocol实例来处理那个客户端的事务。
    # reactor.listenTCP(2556, factory)
    # reactor.run()

    factory = Factory()
    factory.protocol = Transfer
    reactor.listenTCP(2556, factory)
    reactor.run()


if __name__ == '__main__':
    run_server()
    # run()
# ————————————————
# 版权声明：本文为CSDN博主「陈建华呦」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_37923411/article/details/106784033


"""
http://www.ab126.com/goju/1711.html
http://ascii.911cha.com/
"""
