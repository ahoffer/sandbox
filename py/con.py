#! /usr/bin/python

from proton.handlers import MessagingHandler
from proton.reactor import Container

class Recv(MessagingHandler):
    def __init__(self, url):
        super(Recv, self).__init__()
        self.url = url
        self.count = 0;

    def on_start(self, event):
            conn = event.container.connect('10.5.0.7:61616')
            event.container.create_receiver(conn, 'wps.v1.result')
            print("Listening...")

    def on_message(self, event):
        print(event.message.body)
        # print('count={count}\tmsg={body}'.format(count=self.count, body=event.message.body))
        # self.count += 1
try:
    Container(Recv('')).run()
except KeyboardInterrupt:
    pass
