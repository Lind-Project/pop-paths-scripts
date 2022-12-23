#!/bin/bash

# clean up
echo "Init Environment..."
sudo rm -f /hdd/jammy-server-cloudimg-amd64.img  || true
echo "Done"

# server
echo "Init Server..."
screen -mdS "server_screen"
screen -S "server_screen" -p 0 -X stuff "cd pop-paths-scripts/host_scripts && echo $1 | sudo -S  bash ./server.sh 1 ^M"
echo "Done"

# client
echo "Init Server..."
screen -mdS "client_screen"
screen -S "client_screen" -p 0 -X stuff "cd pop-paths-scripts/host_scripts && echo $1 | sudo -S  bash ./setup.sh && echo $1 | sudo -S  bash ./pop_paths.sh ^M"
echo "Done"
