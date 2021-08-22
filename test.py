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
