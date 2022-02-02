#! /usr/bin/python3
import proton
from proton import Message, Connection
from proton.handlers import MessagingHandler
from proton.reactor import Container
import settings
import argparse

parser = argparse.ArgumentParser(description='AMQP client for WPS testing.')
parser.add_argument('role', help='producer or consumer')
parser.add_argument('hosts', nargs='+', help='The name of one or more brokers: live, backup, other')
args = parser.parse_args()

# What does an event know about?
# event.container
# event.connection
# event.session
# event.link
# event.sender
# event.receiver
# event.delivery
# event.message


class Client(MessagingHandler):
    def __init__(self):
        super(Client, self).__init__()
        self.container = None
        self.connection = None
        self.brokers = [settings.all[e] for e in args.hosts]
        self.count = 0

    def on_start(self, event):
        print(self.brokers)
        self.container = event.container
        self.container.container_id = args.role + '-' + '_'.join(args.hosts)
        self.connection = self.container.connect(urls=self.brokers, user='admin', password='admin')
        if args.role == 'consumer':
            event.container.create_receiver(self.connection, source='wps.v1.result')
            print('Waiting...')
        elif args.role == 'producer':
            self.sender = self.container.create_sender(self.connection, 'wps.v1.result')
            self.container.schedule(2, self)
        else:
            print('Did not understand role {role}'.format(role=args.role))
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

    def on_accepted(self, event):
        print("accepted")
        pass

    def on_rejected(self, event):
        print('rejected')

    def on_unhandled(self, name, event):
        # print(name, event)
        pass

    def on_settled(self, event):
        # print('settled')
        pass

    def on_sendable(self, event):
        # print('sendable')
        pass

    def on_disconnected(self, event):
        print("disconnected")

    def on_released(self, event):
        print("released")

    def on_session_error(self, event):
        print('session error')

    def on_transport_error(self, event):
        print("transport error")

    def on_link_error(self, event):
        print("link error")

    def on_connection_closed(self, event):
        print("connection closed")
try:
    Container(Client()).run()
except KeyboardInterrupt:
    pass
