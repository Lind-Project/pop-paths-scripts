#!/bin/bash

# run ltp
sudo timeout 2h bash pop-paths-scripts/pop_paths_scripts/run_ltp.sh 

# generate report
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/full_data