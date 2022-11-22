# installing LTP
sudo apt install gcc git make pkgconf autoconf automake bison flex m4 linux-headers-$(uname -r) libc6-dev
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

#enabling Selinux
sudo python3 pop-paths-scripts/pop_paths_scripts/run_pop_paths.py 1