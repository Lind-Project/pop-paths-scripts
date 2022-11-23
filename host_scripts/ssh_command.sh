#!/bin/bash
if [ $1 -eq 1 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    ssh -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh"
elif [ $1 -eq 2 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    ssh -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh"
elif [ $1 -eq 3 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    ssh -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"
fi