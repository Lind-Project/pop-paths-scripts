sudo bash script.sh $1 &
(
    sudo ./ssh.exp 1
    sleep 10
    sudo ./ssh.exp 2
    sleep 10
    sudo ./ssh.exp 3
)