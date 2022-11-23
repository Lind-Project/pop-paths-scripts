# Resetting all of the data and removing it from the system
sudo rm -r GCOV_DATA
sudo rm -r GCOV_DATA/blank_reset
sudo rm -r GCOV_DATA/pop_paths
sudo rm -r GCOV_DATA/full_data

#creating the directories for the data
mkdir GCOV_DATA
mkdir GCOV_DATA/blank_reset
mkdir GCOV_DATA/pop_paths
mkdir GCOV_DATA/full_data

#resetting the data
sudo echo 0 > /sys/kernel/debug/gcov/reset
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh GCOV_DATA/blank_reset
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 2 #still need to do some automation here

#collecting the pop paths data
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/pop_paths

#trinity and ltp here
timeout 6h run_trinity.sh 
timeout 6h run_ltp.sh 

sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/full_data