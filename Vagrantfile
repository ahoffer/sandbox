# -*- mode: ruby -*-
# vi: set ft=ruby :

# ENV["VAGRANT_EXPERIMENTAL"] = "disks"

Vagrant.configure("2") do |config|

    config.vm.define :live1 do |live1|
    live1.vm.box = "centos/7"
    live1.vm.network :private_network, ip: "10.5.0.3"
    live1.vm.hostname = "live1"
    live1.vm.network "forwarded_port", guest: 8993, host: 18993
#       live1.vm.disk :disk, size: "20GB", primary: true
    live1.vm.provider "virtualbox" do |v|
        v.memory = 8096
        v.cpus = 4
        end
    end

    config.vm.define :backup1 do |backup1|
        backup1.vm.box = "centos/7"
        backup1.vm.network :private_network, ip: "10.5.0.4"
        backup1.vm.network "forwarded_port", guest: 8993, host: 28993
        backup1.vm.hostname = "backup1"
        backup1.vm.provider "virtualbox" do |v|
            v.memory = 8096
            v.cpus = 2
        end
        backup1.vm.provision "shell" do |s|
            # Since I added the "ssh-add -D" command to the clean-install script, this has not been necessary
            ssh_pub_key = File.readlines("#{Dir.pwd}/.ssh/insecure_rsa.pub").first.strip
            s.inline = <<-SHELL
              echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
            SHELL
        end
    end

    config.vm.define :other do |other|
        other.vm.box = "centos/7"
        other.vm.network :private_network, ip: "10.5.0.7"
        other.vm.network "forwarded_port", guest: 8161, host: 18161
        other.vm.hostname = "other"
        other.vm.provider "virtualbox" do |v|
            v.memory = 4096
            v.cpus = 2
        end
    end
end




