from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container


class Send(MessagingHandler):
    def __init__(self, url):
        super(Send, self).__init__()
        self.url = url
        self.sent = 0

    def on_start(self, event):
        self.container = event.container
        self.sender = self.container.create_sender('ampq://10.5.0.7:61616/wps.v1.result')

    def on_sendable(self, event):
        self.container.schedule(2, self)

    def send(self):
        msg = Message(id=(self.sent + 1), body={'sequence': (self.sent + 1)})
        self.sender.send(msg)
        self.sent += 1
        print('Sending {count}\t{body}'.format(count=self.sent, body=msg.body))

    def on_timer_task(self, event):
        self.send()


try:
    Container(Send('')).run()
except KeyboardInterrupt:
    pass
