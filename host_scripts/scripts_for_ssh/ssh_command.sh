#!/bin/bash
if [ $1 -eq 1 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh"; do
    ssh-keygen -N "password" -f /home/tbrigham/key <<<y
    sudo sshpass -p "password" ssh-copy-id -i /home/tbrigham/key.pub -p 2222 -o StrictHostKeyChecking=no ubuntu@localhost
    sudo ssh -i /home/tbrigham/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh"
    #     sleep 10
    # done
elif [ $1 -eq 2 ]
then
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh"; do
    sudo ssh -i /home/tbrigham/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh"
    #     sleep 10
    # done
elif [ $1 -eq 3 ]
then
    sleep 30
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"; do
    sudo ssh -i /home/tbrigham/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"
    #     sleep 10
    # done
elif [ $1 -eq 4 ]
then
    sleep 5
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    echo "HIT HERE"
    # until sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"; do
    # sudo sshpass -p "password" scp -P 2222 -r 'ubuntu@localhost:/home/ubuntu/GCOV_DATA' /hdd/GCOV_DATA/$(date --iso-8601="minutes")
    sudo ./scripts_for_ssh/scp.exp
    #     sleep 10
    echo "HIT HERE TOO"
    # done
fi

