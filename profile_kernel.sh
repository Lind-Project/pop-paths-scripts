#!/bin/bash

########################################################
########            LIND PROJECT                ########
########      Pop-paths data collector          ########
########           Tristan Brigham              ########
########################################################

# to run this program, run it in bash with sudo permissions
# make sure that you have run the config.sh file before running this file

# to monitor progress, run the following command formatted to your situation
# sudo screen -r [client_screen  /  server_screen]

# removing the old server file if we find it in the specified directory
echo "Init Environment..."
sudo rm -f $(cat directory.txt)/jammy-server-cloudimg-amd64.img  || true
echo "Done"

# server
echo "Init Server..."
screen -mdS "server_screen"
screen -S "server_screen" -p 0 -X stuff "cd host_scripts && sudo bash ./server.sh 1 ^M"
echo "Done. See info below."
sudo ls -laR /var/run/screen | grep "server"
echo ""

# client
echo "Init Server..."
screen -mdS "client_screen"
screen -S "client_screen" -p 0 -X stuff "sudo bash host_scripts/run_client.sh^M"
echo "Done. Info below."
sudo ls -laR /var/run/screen | grep "client"
echo ""

