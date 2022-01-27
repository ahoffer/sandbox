# -*- mode: ruby -*-
# vi: set ft=ruby :

# ENV["VAGRANT_EXPERIMENTAL"] = "disks"

def config(name, ip, config)

    config.vm.define name do |config|
        config.vm.box = "centos/7"
        config.vm.network :private_network, ip: ip
        config.vm.hostname =  name
    #       config.vm.disk :disk, size: "20GB", primary: true
        config.vm.synced_folder "./files", "/vagrant"
        config.vm.provider "virtualbox" do |v|
            v.memory = 8096
            v.cpus = 4
            end
        config.vm.provision "shell" do |s|
            # Since I added the "ssh-add -D" command to the clean-install script, this has not been necessary
            ssh_pub_key = File.readlines("#{Dir.pwd}/.ssh/insecure_rsa.pub").first.strip
            s.inline = <<-SHELL
              echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
            SHELL
        end
    end
end

Vagrant.configure("2") do |config|
    config("live1", "10.5.0.3", config)
    config("backup1", "10.5.0.4", config)
    config("other", "10.5.0.7", config)
end





