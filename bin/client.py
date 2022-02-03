#! /usr/bin/python3
from proton import Message
from proton._reactor import DurableSubscription, AtLeastOnce
from proton.handlers import MessagingHandler
from proton.reactor import Container
import settings
import argparse

parser = argparse.ArgumentParser(description='AMQP client for testing.')
parser.add_argument('role', help='producer or consumer')
parser.add_argument('hosts', nargs='+', help='The name of one or more brokers', choices=['live', 'backup', 'other'])
parser.add_argument('-a', help='Address. For example, wps.v1.result', required=True, nargs=1)
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
        self.address = None
        self.receiver = None
        self.container = None
        self.connection = None
        self.brokers = [settings.all[e] for e in args.hosts]
        self.count = 0

    def on_start(self, event):
        print(self.brokers)
        self.address = args.a[0]
        # self.address = "wps.v1.execute.req"
        self.container = event.container
        self.container.container_id = args.role + '-' + '_'.join(args.hosts)
        self.connection = self.container.connect(urls=self.brokers, user='admin', password='admin')
        result = 'sensor.replay'
        if args.role == 'consumer':
            self.receiver = event.container.create_receiver(self.connection, source=self.address)
            DurableSubscription().apply(self.receiver)
            print("Consuming from address " + self.address)
        elif args.role == 'producer':
            self.sender = self.container.create_sender(self.connection, target=self.address)
            AtLeastOnce().apply(self.sender)
            print("Sending to address " + self.address)
            self.container.schedule(2, self)
        else:
            print('Did not understand role {role}'.format(role=args.role))
            exit(1)

    def on_message(self, event):
        print('Receiving\t', event.message)
        # This next part was in the sample code.
        # I don't know enough about connections and closing, and so I commented it out.
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
