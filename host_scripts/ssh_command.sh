sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
ssh -p 2222 ubuntu@localhost