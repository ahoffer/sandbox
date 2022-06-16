# -*- mode: ruby -*-
# vi: set ft=ruby :

# ENV["VAGRANT_EXPERIMENTAL"] = "disks"

def create(name, config)
    config.vm.define name do
#         config.vm.box = "centos7vb"
        config.vm.box = "centos/7"
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
            ssh_pub_key = File.readlines("#{Dir.pwd}/.ssh/insecure_rsa.pub").first.strip
            s.inline = <<-SHELL
              echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
              chmod 640 /home/vagrant/.ssh/authorized_keys
            SHELL
        end
    end
end

Vagrant.configure("2") do |object|
    create("node1", object)
    create("node2", object)
end
