# Resetting all of the data and removing it from the system
sudo rm -r GCOV_DATA

#creating the directories for the data
mkdir GCOV_DATA
mkdir GCOV_DATA/blank_reset
mkdir GCOV_DATA/pop_paths
mkdir GCOV_DATA/full_data

# reset gcov in kernel
sudo bash -c "echo 0 > /sys/kernel/debug/gcov/reset"