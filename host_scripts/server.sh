# making sure that we have the correct libraries installed for cloud images
sudo apt-get install cloud-image-utils

# formatting the correct user data image
cloud-localds server_files/user-data.img server_files/user-data

# check if we should be downloading the server image from the internet
if [ $1 -eq 1 ]
then

    # download the server image
    echo "DOWNLOADING"
    wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img -P /hdd
fi

# resize the image
qemu-img resize /hdd/jammy-server-cloudimg-amd64.img 64G

# start the kvm 
qemu-system-x86_64 -machine accel=kvm -cpu host -drive file=/hdd/jammy-server-cloudimg-amd64.img,format=qcow2 -drive file=server_files/user-data.img,format=raw -m 8G -display none -monitor stdio -net nic,model=e1000 -net user,hostfwd=tcp::2222-:22 -smp cores=14,threads=1,sockets=1