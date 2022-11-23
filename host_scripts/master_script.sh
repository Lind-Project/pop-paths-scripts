# if [ $1 = 1 ] ; then 
#     sleep 30
# else
#     sleep 10
# fi

echo ""
echo "SSHING 1" &&
echo ""
echo ""
sudo bash ssh_command.sh 1 &&
sleep 10 &&

echo ""
echo "SSHING 2" &&
echo ""
echo ""
sudo bash ssh_command.sh 2 &&
sleep 10 &&

echo ""
echo "SSHING 3" &&
echo ""
echo ""
sudo bash ssh_command.sh 3