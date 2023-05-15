source pop-paths-scripts/vars.env
#!/bin/bash
if [ $1 -eq 1 ]
then
    # clean the fingerprint so that we don't have ssh complaining
    # it is fine if the host fingerprint changes since everything is local
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"

    # generate the key for logging into the server
    ssh-keygen -N "" -f ${DIRECTORY}/key <<<y

    # wait for a moment
    sleep 10

    # ssh into the kvm, download this repo, set up app armor, and install the libraries that we need
    sudo sshpass -p "password" ssh-copy-id -i ${DIRECTORY}/key.pub -p 2222 -o StrictHostKeyChecking=no ubuntu@localhost
    
    # wait for a moment for the key to register
    sleep 20
    sudo ssh -i ${DIRECTORY}/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/app_armor_and_intall_packages.sh"

elif [ $1 -eq 2 ]
then
    # clear the fingerprints
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    
    # ssh in, install the kernel, and set up SELinux
    sudo ssh -i ${DIRECTORY}/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash pop-paths-scripts/pop_paths_scripts/install_kernel_trinity_ltp.sh"

elif [ $1 -eq 3 ]
then
    # clear the fingerprints
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
    
    # ssh in and run the scripts for collecting requisite data
    sudo ssh -i ${DIRECTORY}/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash pop-paths-scripts/pop_paths_scripts/collect_data.sh"

elif [ $1 -eq 4 ]
then
    # clear the fingerprints
    sleep 5
    sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
    sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"

    echo "Making the directory for the data"

    # create a holding directory if it hasn't been created yet
    sudo mkdir -p ${DIRECTORY}/GCOV_DATA;
    
    # create a ../directory for holding our data
    sudo mkdir ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")

    echo "Retrieving the data"

    # retrieve the data from the kvm machine
    sudo scp -r -i ${DIRECTORY}/key -o StrictHostKeyChecking=no -P 2222 ubuntu@localhost:/home/ubuntu/GCOV_DATA ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")
    
    echo "Zero the Data"

    # zero-out all of the data in the kernel
    sudo ssh -i ${DIRECTORY}/key -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "bash ./pop-paths-scripts/pop_paths_scripts/gcov_data_helpers/reset_data.sh"

    # now generate the analyzer file in the folder with the GCOV data
    python ./pop-paths-scripts/pop_paths_scripts/analyzer.py -i ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/GCOV_DATA/full_data/kernel.info  -o ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/FULL_RUN_COVERAGE.txt
    python ./pop-paths-scripts/pop_paths_scripts/analyzer.py -i ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/GCOV_DATA/pop_paths/kernel.info  -o ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/POP_PATHS_COVERAGE.txt
    python ./pop-paths-scripts/pop_paths_scripts/analyzer.py -i ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/GCOV_DATA/blank_reset/kernel.info  -o ${DIRECTORY}/GCOV_DATA/$(date --iso-8601="minutes")/BLANK_RESET_COVERATE.txt
    
fi

