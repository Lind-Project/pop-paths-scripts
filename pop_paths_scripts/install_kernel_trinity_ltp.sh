source vars.env

# installing LTP
sudo apt-get install --assume-yes gcc git make pkgconf autoconf automake bison flex m4 linux-headers-$(uname -r) libc6-dev
git clone https://github.com/linux-test-project/ltp.git
cd ltp

# making the LTP app and installing it
make autotools
./configure
sudo make all
sudo make install
cd ..

# installing trinity
git clone https://github.com/kernelslacker/trinity.git
cd trinity
./configure
make
cd ..

# downloading the kernel
# wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/linux/5.11.0-49.55/linux_5.11.0.orig.tar.gz -O kernel.tar.gz
wget ${KERNEL_LINK} -O kernel.tar.gz
mkdir kernel_out

# un-tarring the kernel
tar -xvf kernel.tar.gz --strip 1 -C kernel_out
cd kernel_out/
sudo apt-get install --assume-yes libncurses-dev flex bison openssl libssl-dev dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf lcov expect

# making the kernel
timeout 5s make menuconfig
sudo cp ../pop-paths-scripts/pop_paths_scripts/extra_files/BIG_CONFIG.config ./.config
sudo make -j $(nproc)
sudo make modules_install -j $(nproc)
sudo make install -j $(nproc)
cd ..

# updating the grub so that it points to the right kernel on restart
echo $(python3 ./pop-paths-scripts/pop_paths_scripts/get_kernel_name.py) >> pop-paths-scripts/pop_paths_scripts/extra_files/grub_in
sudo cp pop-paths-scripts/pop_paths_scripts/extra_files/grub_in /etc/default/grub
sudo update-grub

#enabling Selinux
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 1
