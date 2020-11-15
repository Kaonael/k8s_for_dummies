ansible-playbook -i hosts.ini gitlab.yml

ansible-playbook -i hosts.ini microk8s.yml --extra-vars "ci_token=foo"

ansible-playbook -i hosts.ini gitlab_runner.yml --extra-vars "registration_token=foo"