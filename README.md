Run Playbook

[//]: # (ansible-playbook --private-key .ssh/insecure_rsa -u vagrant -i inventory.ini playbook.yml )

ansible-playbook playbook.xml

TODO: Install RPM package on Reflex instances

./artemis consumer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.5.0.3:5672' --user admin --password admin --verbose

./artemis consumer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.7.0.3:5672' --user admin --password admin --verbose


<connector name="netty-connector">tcp://localhost:61616</connector>



./artemis producer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.5.0.3:5672' --user admin --password admin  --sleep 2000 --message-size 128 --verbose