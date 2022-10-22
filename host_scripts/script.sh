sudo apt-get install cloud-image-utils

cloud-localds user-data.img user-data

# wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

qemu-img resize jammy-server-cloudimg-amd64.img +128G

qemu-system-x86_64 -machine accel=kvm -cpu host -drive file=jammy-server-cloudimg-amd64.img,format=qcow2 -drive file=user-data.img,format=raw -m 8G -display none -monitor stdio -net nic,model=e1000 -net user,hostfwd=tcp::2222-:22 -smp cores=14,threads=1,sockets=1


