#! /usr/bin/python3
import subprocess, re, argparse
parser = argparse.ArgumentParser(description='Consume messages from wps.v1.result.')
parser.add_argument('-u', '--url', nargs='?', help='tcp://10.5.0.7:61616', default = '(tcp://10.5.0.3:5672,tcp://10.5.0.4:5672)?ha=true')
args = parser.parse_args()
r_uuid = re.compile('[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')
r_msg = re.compile('Received .*')
count =0
print("Starting...")
while True:
    cmd = f'artemis consumer --destination topic://wps.v1.result --message-count 1 --url "{args.url}" --user admin --password admin --verbose'
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    str_out = out.stdout.decode('utf-8')
    m_uuid = r_uuid.search(str_out)
    m_msg = r_msg.search(str_out)
    str_msg=m_msg.group().split('Received ')[1]
    str_uuid = m_uuid.group()
    count += 1
    extra = f'consuming msg={str_msg}     ' if str_uuid not in str_msg else ''
    print(f'count={count}   {extra}uuid={str_uuid}')
