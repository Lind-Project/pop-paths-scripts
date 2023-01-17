#!/bin/bash
if [ $1 -eq 1 ]
then
    # clean the fingerprint so that we don't have ssh complaining
    # it is fine if the host fingerprint changes since everything is local
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"

    # generate the key for logging into the server
    ssh-keygen -N "" -f $(cat ../directory.txt)/key <<<y

    # wait for a moment
    sleep 10

    # ssh into the kvm, download this repo, set up app armor, and install the libraries that we need
    sudo sshpass -p "password" ssh-copy-id -i $(cat ../directory.txt)/key.pub -p 2222 -o StrictHostKeyChecking=no ubuntu@localhost
    
    # wait for a moment for the key to register
    sleep 20
    sudo ssh -i $(cat ../directory.txt)/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/app_armor_and_intall_packages.sh"

elif [ $1 -eq 2 ]
then
    # clear the fingerprints
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    
    # ssh in, install the kernel, and set up SELinux
    sudo ssh -i $(cat ../directory.txt)/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash pop-paths-scripts/pop_paths_scripts/install_kernel_trinity_ltp.sh"

elif [ $1 -eq 3 ]
then
    # clear the fingerprints
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    
    # ssh in and run the scripts for collecting requisite data
    sudo ssh -i $(cat ../directory.txt)/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash pop-paths-scripts/pop_paths_scripts/collect_data.sh"

elif [ $1 -eq 4 ]
then
    # clear the fingerprints
    sleep 5
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"

    # create a holding directory if it hasn't been created yet
    sudo mkdir -p $(cat ../directory.txt)/GCOV_DATA;
    
    # create a ../directory for holding our data
    sudo mkdir $(cat ../directory.txt)/GCOV_DATA/$(date --iso-8601="minutes")

    # retrieve the data from the kvm machine
    sudo scp -r -i $(cat ../directory.txt)/key -o StrictHostKeyChecking=no -P 2222 ubuntu@localhost:/home/ubuntu/GCOV_DATA $(cat ../directory.txt)/GCOV_DATA/$(date --iso-8601="minutes")
    
    # zero-out all of the data in the kernel
    sudo ssh -i $(cat ../directory.txt)/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash ./pop-paths-scripts/pop_paths_scripts/gcov_data_helpers/reset_data.sh"
fi

