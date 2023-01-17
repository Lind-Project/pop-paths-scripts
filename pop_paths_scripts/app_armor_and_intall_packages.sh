sudo apt-get update

# installing packages using our custom script
sudo bash pop-paths-scripts/pop_paths_scripts/install_script.sh

# updating the timeout values so that ssh doesn't die on us
sudo cp pop-paths-scripts/pop_paths_scripts/extra_files/sshd_config /etc/ssh/sshd_config

# restarting and updating ssh service
sudo service sshd restart

# disabling App Armor
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 0