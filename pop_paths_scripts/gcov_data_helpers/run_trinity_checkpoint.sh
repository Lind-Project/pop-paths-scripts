#!/bin/bash

#trinity here
timeout 10s bash pop-paths-scripts/pop_paths_scripts/run_trinity.sh 

# call another script that runs ltp and then calls other scripts
# so that if we fail during trinity, we can easily pick back up where we left off
# by running the command in the sequence again
bash ./pop-paths-scripts/pop_paths_scripts/gcov_data_helpers/run_ltp_checkpoint.sh
