from sys import stdout

from twisted.internet.protocol import Protocol, Factory, ClientCreator, ClientFactory
from twisted.internet import reactor, protocol

PORT = 2556


class FakeTelnet(Protocol):

    def dataReceived(self, data):
        print(data)
        print(self.transport.write(data))

    def connectionMade(self):
        self.otherFact = protocol.ClientFactory()
        self.otherFact.protocol = EchoClient
        self.factory.clients.append(self.otherFact.protocol)
        reactor.connectTCP('psrfb6', 10999, self.otherFact)

    def dataReceived(self, data):
        print('data', data)
        print('data', data.decode('utf-8', 'ignore'))
        for client in self.factory.clients:
            client.transport.write('START\r\n')

        # if 'START' in data:
        #     # send a command to cookie server.
        #     for client in self.factory.clients:
        #         client.transport.write('START\r\n')

    def connectionLost(self):
        print('connection lost')


class EchoClient(Protocol):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):
        print("Connection to cookie server")

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Fortune Server said:", data)

    def connectionLost(self, reason):
        print("connection lost")

    def send_stuff(self, data):
        self.transport.write(data)


class MyFactory(Factory):
    protocol = FakeTelnet

    def __init__(self, EchoClient):
        self.clients = []
        self.otherCli = EchoClient


""""""


class Echo(Protocol):
    def dataReceived(self, data):
        # stdout.write(data)
        for client in self.factory.clients:
            print('client', client)
            client.transport.write('127.0.0.1 FML2 junsi\r\n')


class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print('Started to connect.')

        # stdout.write('127.0.0.1 FML2 junsi')

    def buildProtocol(self, addr):
        print('Connected.', addr)

        return Echo()

    def clientConnectionLost(self, connector, reason):
        print('Lost connection. Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)


if __name__ == '__main__':
    # factory = Factory()  # 实例化Factory
    # factory.protocol = EchoProtocol  # 设置factory的protocol属性以便它知道使用哪个protocol与客户端通信(这就是所谓的你的自定义protocol)

    # reactor.listenTCP(PORT, MyFactory(EchoClient))
    # reactor.run()

    reactor.connectTCP('127.0.0.1', 25565, EchoClientFactory())
    reactor.run()
