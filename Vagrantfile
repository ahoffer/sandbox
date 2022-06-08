# -*- mode: ruby -*-
# vi: set ft=ruby :

# ENV["VAGRANT_EXPERIMENTAL"] = "disks"

def create(name, ip, config)
    config.vm.define name do
        config.vm.box = "centos7vb"
        config.vbguest.installer_options = { allow_kernel_upgrade: true }
        config.vm.network :private_network, type: "dhcp"
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
#     config("live", "192.168.63.7", config)
#     config("backup", "192.168.63.8", config)
    create("node1", "10.5.0.3", config)
    create("node2", "10.5.0.4", config)
#     config("other", "10.5.0.7", config)
end
