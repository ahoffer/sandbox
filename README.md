Run Playbook

## Getting Started

### Run Vagrant and Ansible

Automate as much as possible.

```
vagrant destroy --force;vagrant up && ansible-playbook playbook.yml playbook.yml
```

### Configure Live and Backup

Run the `opt/reflex/bin/configure-cluster.sh` file as root or as reflex on both live and backup VMs.
Use IP addresses instead of hostnames.

### Visit Web Consoles

* http://10.5.0.7:8161/
* https://10.5.0.3:8993/hawtio


./artemis producer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.5.0.3:5672' --user admin --password admin  --sleep 2000 --message-size 128 --verbose

### Start producers or consumers

There are scripts on the path in the machine "other" for producers and consumers.
A producer sends messages to the wps.v1.result address. 
A consumer receives messages from that address.
The producer and consumer scripts are separated by which broker (live, backup, other) the messages are sent to, or received from.

`prodlive`, `prodlive`, `prodother`
`conlive`, `conlive`, `conother`


## NOTES
* Added netty-connector to downstream Artemis (other). I don't know if that was required or not. Something to test, maybe.
* `<connector name="netty-connector">tcp://localhost:61616</connector>`

```
./artemis consumer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.5.0.3:5672' --user admin --password admin --verbose

./artemis consumer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.7.0.3:5672' --user admin --password admin --verbose
```


## Misc

Explicit use of ansible
```
ansible-playbook --private-key .ssh/insecure_rsa -u vagrant -i inventory.ini playbook.yml 
```