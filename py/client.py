#! /usr/bin/python3
from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container
import settings
import argparse

parser = argparse.ArgumentParser(description='AMQP client for WPS testing.')
parser.add_argument('roles', help='The name of one or more brokers: live, backup, other')
parser.add_argument('hosts', nargs='+', help='sum the integers (default: find the max)')
args = parser.parse_args()

class Recv(MessagingHandler):
    def __init__(self):
        super(Recv, self).__init__()
        self.container = None
        self.connection = None
        self.brokers = [settings.all[e] for e in args.hosts]
        self.count = 0

    def on_start(self, event):
        print(self.brokers)
        self.container = event.container
        self.connection = self.container.connect(urls=self.brokers, user='admin', password='admin')
        if args.roles == 'consumer':
            event.container.create_receiver(self.connection, source='wps.v1.result')
            print('Waiting...')
        elif args.roles == 'producer':
            self.sender = self.container.create_sender(self.connection, 'wps.v1.result')
            self.container.schedule(2, self)
        else:
            print('Did not understand roles {roles}'.format(roles=args.roles))
            exit(1)

    def on_message(self, event):
        print('Receiving\t', event.message)
        # if event.receiver.queued == 0 and event.receiver.drained:
        #     print('Nothing queued')
        #     event.connection.close()

    def send(self):
        msg = Message(id=(self.count + 1), body={'sequence': (self.count + 1)})
        self.sender.send(msg)
        self.count += 1
        print('Sending {count}\t{body}'.format(count=self.count, body=msg.body))
        self.container.schedule(2, self)

    def on_timer_task(self, event):
        self.send()

try:
    Container(Recv()).run()
except KeyboardInterrupt:
    pass
