echo ""
echo "SSHING 3"
echo ""
echo ""
sudo bash ./ssh_command.sh 3

echo ""
echo "RETRIEVING FOLDERS"
echo ""
echo ""
sudo bash ./ssh_command.sh 4

echo ""
echo "DELETING KVM AND CREATED FILES"
echo ""
echo ""
sudo rm -f /hdd/jammy-server-cloudimg-amd64.img  || true