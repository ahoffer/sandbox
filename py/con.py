#! /usr/bin/python

from proton.handlers import MessagingHandler
from proton.reactor import Container

class Recv(MessagingHandler):
    def __init__(self):
        super(Recv, self).__init__()

    def on_start(self, event):
        self.connection = event.container.connect('10.5.0.7:61616/wps.v1.result', user='admin', password='admin')
        event.container.create_receiver(self.connection, source='wps.v1.result')

    def on_message(self, event):
        print(event.message)
        # if event.receiver.queued == 0 and event.receiver.drained:
        #     print('Nothing queued')
        #     event.connection.close()


Container(Recv()).run()


# try:
#     Container(Recv('')).run()
# except KeyboardInterrupt:
#     pass
