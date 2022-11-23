sudo bash script.sh $1 &
(
    ./ssh.exp 1
    sleep 10
    ./ssh.exp 2
    sleep 10
    ./ssh.exp 3
)