from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


class HelloWorld(MessagingHandler):
    def __init__(self, urls, address):
        super(HelloWorld, self).__init__()
        self.urls = urls
        self.address = address

    def on_start(self, event):
        conn = event.container.connect(urls=self.urls)
        event.container.create_receiver(conn, self.address)
        event.container.create_sender(conn, self.address)

    def on_sendable(self, event):
        event.sender.send(Message(body="Hello World!"))
        event.sender.close()

    def on_message(self, event):
        print(event.message.body)
        event.connection.close()


Container(HelloWorld(['10.5.0.7:61616'], "wps.v1.result")).run()