Vagrant.configure("2") do |config|
    config.ssh.insert_key = false

    config.vm.provider "virtualbox" do |v|
        v.memory = 3072
        v.cpus = 2
    end

    config.vm.define "minikube" do |minikube|
        config.vm.box = "bento/ubuntu-20.04"

        minikube.vm.network "private_network", ip: "192.168.50.10"
        minikube.vm.hostname = "minikube"
        minikube.vm.provision "ansible" do |ansible|
            ansible.playbook = "minikube_setup_playbook.yml"
        end
        config.vm.provision "setup_prometheus", type: "ansible", run: "never" do |ansible|
            ansible.playbook = "setup_prometheus_operator_playbook.yml"
        end
    end
end