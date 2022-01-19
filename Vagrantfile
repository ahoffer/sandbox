# -*- mode: ruby -*-
# vi: set ft=ruby :

# ENV["VAGRANT_EXPERIMENTAL"] = "disks"

Vagrant.configure("2") do |config|

      config.vm.define :live1 do |live1|
      live1.vm.box = "centos/8"
      live1.vm.network :private_network, ip: "10.5.0.3"
      live1.vm.hostname = "live1"
#       live1.vm.disk :disk, size: "20GB", primary: true
      live1.vm.provider "virtualbox" do |v|
            v.memory = 8096
            v.cpus = 4
      end
  end

    config.vm.define :backup1 do |backup1|
        backup1.vm.box = "centos/8"
        backup1.vm.network :private_network, ip: "10.5.0.4"
        backup1.vm.hostname = "backup1"
        backup1.vm.provider "virtualbox" do |v|
            v.memory = 8096
            v.cpus = 2
        end
    end

    config.vm.define :other do |other|
        other.vm.box = "centos/8"
        other.vm.network :private_network, ip: "10.5.0.7"
        other.vm.hostname = "other"
        other.vm.provider "virtualbox" do |v|
            v.memory = 4096
            v.cpus = 2
        end
    end
end




