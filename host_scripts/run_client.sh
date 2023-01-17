# wait for the vm to initialize
sleep 300 

# run the setup script
cd host_scripts 
bash ./setup.sh 

# wait for the vm to restart and get all of the data
sleep 300 
bash ./pop_paths.sh 

echo ""
echo "DELETING KVM AND CREATED FILES"
echo ""
echo ""
sudo rm -f $(cat directory.txt)/jammy-server-cloudimg-amd64.img  || true