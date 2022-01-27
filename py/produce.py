#! /usr/bin/python3

import subprocess, re, argparse, datetime
default = '(tcp://10.5.0.3:5672,tcp://10.5.0.4:5672)?ha=true'
parser = argparse.ArgumentParser(description='Publish messages to wps.v1.result.')
parser.add_argument('-u', '--url', nargs='?', help=default, default = default)
parser.add_argument('-m','--msg', nargs='?', help='Content of message', default = datetime.datetime.now())
args = parser.parse_args()
count =0
print("Publishing...")
r_msg = re.compile('Sent:?\s?.*')
cmd = f"""
artemis producer \
--destination 'topic://wps.v1.result' \
--message-count 1 \
--message "{args.msg}" \
--url "{args.url}" \
--user admin \
--password admin \
--sleep 2000 \
--verbose
"""
while True:
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    str_out = out.stdout.decode('utf-8')
    m_msg = r_msg.search(str_out)
    str_msg=m_msg.group().split('Sent: ')[1]
    count += 1
    print(f'count={count}    publishing msg={str_msg}')
