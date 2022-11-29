#!/bin/bash
if [ $1 -eq 1 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh"; do
    sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh"
    #     sleep 10
    # done
elif [ $1 -eq 2 ]
then
    sleep 30
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh"; do
    sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh"
    #     sleep 10
    # done
elif [ $1 -eq 3 ]
then
    sleep 30
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"; do
    sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"
    #     sleep 10
    # done
elif [ $1 -eq 4 ]
then
    sleep 5
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    echo "HIT HERE"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"; do
    sudo sshpass -p "password" sudo scp -P 2222 -r 'ubuntu@localhost:/home/ubuntu/GCOV_DATA' '/hdd/GCOV_DATA/$(date --iso-8601="minutes")'
    #     sleep 10
    # done
fi