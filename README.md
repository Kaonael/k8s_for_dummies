ansible-playbook -i hosts.ini gitlab.yml
ansible-playbook -i hosts.ini gitlab_runner.yml --extra-vars "registration_token=foo"