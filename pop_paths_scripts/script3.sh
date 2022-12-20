sudo bash ./pop-paths-scripts/pop_paths_scripts/script3/reset_data.sh

sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh GCOV_DATA/blank_reset
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 2 

ls -ahl /hdd > /home/tbrigham/log5.txt

#collecting the pop paths data
sudo bash pop-paths-scripts/pop_paths_scripts/makeReport.sh ./GCOV_DATA/pop_paths

ls -ahl /hdd > /home/tbrigham/log6.txt

# call another script that runs trinity and then calls other scripts
# so that if we fail during trinity, we can easily pick back up where we left off
# by running the command in the sequence again
bash ./pop-paths-scripts/pop_paths_scripts/script3/run_trinity_checkpoint.sh