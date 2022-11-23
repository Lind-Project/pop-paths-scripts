# if [ $1 = 1 ] ; then 
#     sleep 30
# else
#     sleep 10
# fi

echo "SSHING 1"
sudo ./ssh.exp 1 &&
sleep 10 &&

echo "SSHING 2"
sudo ./ssh.exp 2 &&
sleep 10 &&

echo "SSHING 3"
sudo ./ssh.exp 3 