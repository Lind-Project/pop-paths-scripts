# installing LTP
sudo apt-get install --assume-yes gcc git make pkgconf autoconf automake bison flex m4 linux-headers-$(uname -r) libc6-dev
git clone https://github.com/linux-test-project/ltp.git
cd ltp
make autotools
./configure
sudo make all
sudo make install
cd ..

#installing trinity
git clone https://github.com/kernelslacker/trinity.git
cd trinity
./configure
make
cd ..

#downloading the kernel
wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/linux/5.11.0-49.55/linux_5.11.0.orig.tar.gz
tar -xvf linux_5.11.0.orig.tar.gz 
cd linux-5.11/
sudo apt-get install --assume-yes libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf lcov expect

# making the kernel
timeout 5s make menuconfig
sudo cp ../pop-paths-scripts/pop_paths_scripts/extra_files/BIG_CONFIG.config ./.config
sudo make -j 4
sudo make modules_install
sudo make install
cd ..
sudo cp pop-paths-scripts/pop_paths_scripts/extra_files/grub_in /etc/default/grub

# deleting the kernel file (because it is obscenely large)
sudo rm -r /home/ubuntu/linux-5.11

#enabling Selinux
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 1