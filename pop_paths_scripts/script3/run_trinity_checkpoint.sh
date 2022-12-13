#!/bin/bash

#trinity here
timeout 6h bash pop-paths-scripts/pop_paths_scripts/run_trinity.sh 

ls -ahl /hdd > /home/tbrigham/log1.txt

# call another script that runs ltp and then calls other scripts
# so that if we fail during trinity, we can easily pick back up where we left off
# by running the command in the sequence again
./pop-paths-scripts/pop_paths_scripts/script3/run_ltp_checkpoint.sh
