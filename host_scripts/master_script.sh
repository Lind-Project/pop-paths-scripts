# if [ $1 = 1 ] ; then 
#     sleep 30
# else
#     sleep 10
# fi

echo "SSHING 1"
sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "git clone https://github.com/Lind-Project/pop-paths-scripts.git && bash pop-paths-scripts/pop_paths_scripts/script1.sh" && 
sleep 10 &&

echo "SSHING 2"
sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script2.sh" && 
sleep 10 &&

echo "SSHING 3"
sudo ssh-keygen -f "/home/tbrigham/.ssh/known_hosts" -R "[localhost]:2222"
sudo ssh-keygen -f "/root/.ssh/known_hosts" -R "[localhost]:2222"
sudo sshpass -p "password" ssh -o StrictHostKeyChecking=no -p 2222 ubuntu@localhost "sudo bash pop-paths-scripts/pop_paths_scripts/script3.sh"