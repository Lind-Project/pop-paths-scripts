# reset the gcov data
sudo bash ./pop-paths-scripts/pop_paths_scripts/gcov_data_helpers/reset_data.sh

# get the initial gcov data
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/blank_reset

# run the pop paths
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 2 

#collecting the pop paths data
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/pop_paths

# call another script that runs trinity and then calls other scripts
# so that if we fail during trinity, we can easily pick back up where we left off
# by running the command in the sequence again
bash ./pop-paths-scripts/pop_paths_scripts/gcov_data_helpers/run_trinity_checkpoint.sh

# generate report
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/full_data