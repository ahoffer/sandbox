# NOTES: It works. By God, it works!

import time

import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame)

    def on_message(self, frame):
        print('received a message "%s"' % frame)


hosts = [('10.5.0.7', 61616)]

conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)
conn.subscribe(destination='wps.v1.result', id=1, ack='auto')

# for i in range(20):
#     print('Sending message ', i)
#     conn.send(body='tire buyer', destination='wps.v1.result')
#     time.sleep(2)

while True:
    time.sleep(10)

conn.disconnect()
