Run Playbook

## Getting Started

### Run Vagrant and Ansible

Automate as much as possible.

```
vagrant destroy --force;vagrant up && ansible-playbook playbook.yml playbook.yml
```

### Configure Live and Backup

Run the `opt/reflex/bin/configure-cluster.sh` file as root or as reflex on both live and backup VMs.
Use IP addresses instead of hostnames. Use "admin" for all usernames and password.

### Visit Web Consoles

* http://10.5.0.7:8161/
* https://10.5.0.3:8993/hawtio


./artemis producer --destination topic://wps.v1.result --message-count 99999999 --url 'tcp://10.5.0.3:5672' --user admin --password admin  --sleep 2000 --message-size 128 --verbose

### Start producers or consumers

There are scripts on the path in the machine "other" for producers and consumers.
A producer sends messages to the wps.v1.result address. 
A consumer receives messages from that address.
The producer and consumer scripts for either for the cluster (live + backup) or the "other" broker.


### Configure Federation
Create a file from this text:

```json
{
    "addresses": [
        "unicorn.v1.observation", 
        "wps.v1.result"
    ], 
    "adressPolicyName": "addressPolicy", 
    "name": "wps", 
    "policySetName": "policySet", 
    "sites": [
        {
            "direction": "downstream", 
            "name": "second", 
            "password": "ENC(-4db652271cf8b661)", 
            "url_backup": "", 
            "url_live": "tcp://10.5.0.7:5672", 
            "user": "admin"
        }
    ]
}
```

Use the `import-federation-files` script to import the file into the live and backup Reflex instances.

```
./import-federation-files wps.json -b ../../etc/artemis.xml
```

# Commands

Open console `./term`
Use shortcuts 'start', 'stop', 'restart', and 'log' on the live and backup VMs


## Misc

Explicit use of ansible
```
ansible-playbook --private-key .ssh/insecure_rsa -u vagrant -i inventory.ini playbook.yml 
```