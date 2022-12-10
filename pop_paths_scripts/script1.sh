sudo apt-get update

# installing packages
sudo bash pop-paths-scripts/pop_paths_scripts/install_script.sh

# updating the timeout values
sudo cp pop-paths-scripts/pop_paths_scripts/extra_files/sshd_config /etc/ssh/sshd_config
sudo service sshd restart

# disabling App Armor
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 0