sudo apt-get install cloud-image-utils

cloud-localds user-data.img user-data

if [ $1 -eq 1 ]
then
    echo "DOWNLOADING"
    wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img -P /home/tbrigham
fi

qemu-img resize /home/tbrigham/jammy-server-cloudimg-amd64.img +128G

qemu-system-x86_64 -machine accel=kvm -cpu host -drive file=/home/tbrigham/jammy-server-cloudimg-amd64.img,format=qcow2 -drive file=user-data.img,format=raw -m 8G -display none -monitor stdio -net nic,model=e1000 -net user,hostfwd=tcp::2222-:22 -smp cores=14,threads=1,sockets=1

