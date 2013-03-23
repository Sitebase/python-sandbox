# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box       = 'precise64'
  config.vm.box_url   = 'http://files.vagrantup.com/precise64.box'

  config.vm.network :hostonly, "192.168.33.13"

  #config.vm.share_folder "v-webapps", "/vagrant/webapps", "webapps"
  config.vm.share_folder "v-app", "/vagrant/app", "app"
  config.vm.share_folder "v-logs", "/vagrant/logs", "logs"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.module_path = "puppet/modules"
    #puppet.options = ['--verbose --debug']
    puppet.options = ['--verbose']
  end

end
