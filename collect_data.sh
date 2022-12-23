#!/bin/bash

########################################################
########            LIND PROJECT                ########
########      Pop-paths data collector          ########
########           Tristan Brigham              ########
########################################################

# to run this program, run it in bash with sudo permissions
# it requires your password as the first command line argument
# to set up the screens

# to monitor progress, run the following command formatted to your situation
# sudo screen -r [client_screen  /  ]
# screen_id is the number before the period wh

# clean up
echo "Init Environment..."
sudo rm -f /hdd/jammy-server-cloudimg-amd64.img  || true
echo "Done"

# server
echo "Init Server..."
screen -mdS "server_screen"
screen -S "server_screen" -p 0 -X stuff "cd host_scripts && sudo bash ./server.sh 1 ^M"
echo "Done. See info below"
sudo ls -laR /var/run/screen | grep "server"

# client
echo "Init Server..."
screen -mdS "client_screen"
screen -S "client_screen" -p 0 -X stuff "sleep 140 && cd host_scripts && bash ./setup.sh && bash ./pop_paths.sh ^M"
echo "Done"
sudo ls -laR /var/run/screen | grep "client"

