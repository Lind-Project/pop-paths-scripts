#Author: Tristan Brigham (TristanB22) 

''' To Run:

1) Run a command that uses sudo (try "sudo ls")
2) In the same bash prompt, once that command is done, run this
    This ensures that the commands in this script has root privileges without you needing to input the password again

'''
apparmor_stop=[ #we need to run this before installing selinux because apparmor and selinux conflict
    "sudo systemctl stop apparmor",
    "sudo apt-get remove apparmor -y",
    "sudo reboot now",
]

selinux_install=[ #the commands for installing and starting selinux
    "sudo apt install policycoreutils selinux-utils selinux-basics",
    "sudo selinux-activate",
    "sudo selinux-config-enforcing"
    "sudo reboot now",
]

import os
import time

mount_file_name="./pop-paths-scripts/mnt_file"
bash_script_file=os.getcwd()+"/pop-paths-scripts/bash_script.sh"
perl_script_file=os.getcwd()+"/pop-paths-scripts/perl_script"
script2=os.getcwd()+"/pop-paths-scripts/cscript2.cpp"
c_command_line_args=os.getcwd()+"/pop-paths-scripts/cscript.c"
function_slang=os.getcwd()+"/pop-paths-scripts/slang"
python_mount_script=os.getcwd()+"/pop-paths-scripts/mount.py {}".format(mount_file_name)
print(os.getcwd())

# just using the command line hits libss2 and readline-common

commands = [
    "sudo apt-get install -y libconfig-dev libedit-dev curl libreadline6-dev slsh", 
    "curl https://www.jedsoft.org/fun/complex/fztopng/fztopng -o ./fztopng", #getting script for slang
    "chmod +x fztopng",
    "sudo ./fztopng -x -8:8:#512 -y -2:2:#128 -o sin_hsv.png -f 'sin(z)'", #testing slang
    "sudo ./fztopng -x -8:8:#512 -y -2:2:#128 -o sin_hsv.png -f {}".format(function_slang),
    "cp /usr/share/common-licenses/GPL-3 .", #testing PCRE
    "grep '^GNU' GPL-3",
    "grep '^[A-Z]' GPL-3",
    "grep '([A-Za-z ]*)' GPL-3",
    "grep -E '(GPL|General Public License)' GPL-3",
    "grep -E '[[:alpha:]]{16,20}' GPL-3",
    "echo '{}' > c.c".format(c_command_line_args), #testing libpopt0 (command line arguments)
    "gcc -o ./ex c.c",
    "./ex 'hello'",
    "sudo dd if=/dev/zero of=loopbackfile.img bs=1M count=10", #testing mount for the next several lines
    "sudo losetup -f loopbackfile.img",
    "sudo losetup -a | grep 'loopbackfile.img' > '{}'".format(mount_file_name),
    "sudo mkfs.ext4 $(python {})".format(python_mount_script),
    "sudo mkdir /media/loop100",
    "sudo mount $(python {}) /media/loop100".format(python_mount_script),
    "sudo umount /media/loop100",
    "losetup -d $(python {})".format(python_mount_script),
    "rm loopbackfile.img",
    "bzip2 -zfk -vv --best test_file.txt", #zipping files to test libbz2-1.0
    "bzip2 -t -vv --best test_file.txt.bz2",
    "bzip2 -df -vv --fast test_file.txt.bz2",
    "blkid -gksu raid --output full -S 1000", #using blkid command to test libblkid1
    "echo 'this is a tempfile' > ~/Desktop/tempFile.txt",
    "wall ~/Desktop/tempFile.txt", #testing bsdutils
    "vim -c 'q' ~/Desktop/tempFile.txt",
    "sudo adduser --disabled-password --gecos '' lind2", #testing libpam-modules and libpam0g and adduser
    "sudo passwd lind2", #testing passwd and lsb-base
    "sudo userdel lind2",
    "dir ~/Desktop",
    "cp ./test_file.txt ./test2.txt",
    "mkdir ./temp_dir", 
    "rmdir ./temp_dir", #using rmdir to test coreutils
    "printenv",
    "sleep 3",
    "pwd", #testing lsb-base
    "ps -aux", #testing procps
    "last", #testing sysvinit-utils
    "lastb", #testing sysvinit-utils
    "mesg y", 
    "mesg n",
    "kill 100000", #testing util-linux
    "whoami",
    "id", #testing lsb-base
    "who",
    "ln -s file2.txt file3.txt",
    "ls -l file3.txt",
    "uuidgen -t", #testing libuuid and util-linux
    "uuidgen -r",
    "echo 'ls -ahl' > ./script.sh",
    "sudo debconf -p medium --frontend=readline sh -x ./script.sh",
    "chmod u-rw ./test2.txt", #using chmod command to test libacl
    "chmod a=rwx ./test2.txt",
    "bash -c 'echo helloThere'",
    "bash -i 'echo helloThere'",
    "sudo apt-get -y install cpp-8",  #using apt command to test dpkg and apt
    "sudo apt-get -y remove cpp-8",
    "tar -zcvf ~/Desktop/tarred_information.tar.gz ~/Desktop/fuzzing", #using tar gz to test zlib1g and tar and gz
    "cat 'hellohellohellohellohello\n this is linux and I really like the operating system\nit is just interesting that it is taking so long to fuzz it' > ~/Desktop/info.txt", #testing lsb-base
    "sed 's/linux/unix' ~/Desktop/info.txt", #testing sed
    "sed 's/hello/aloha/2' ~/Desktop/info.txt",
    "md5sum ~/Desktop/info.txt",
    "cksum ~/Desktop/info.txt",
    "time cat ~/Desktop/info.txt",
    "time ls",
    "time pwd",
    "chmod +xrw {}".format(bash_script_file), #testing bash
    "bash {}".format(bash_script_file),
    "chmod +x {}".format(perl_script_file),#testing perl-base
    "./{}".format(perl_script_file),
    "echo 'Welcome To Lind' | sed 's/\([A-Z]\)/\(\1\)/g'",
    "printenv",
    "pwd",
    "ls",
    "sudo apt install lsb-core", #testing debconf
    "lsb_release -a",
    "which pwd", #testing debianutils
    "which cat", #testing debianutils
    "which ls", #testing debianutils
    "mktemp -u",
    "mktemp -d",
    "mktemp",
    "savelog -Cdt ./log_file", #testing debianutils
    "run-parts --list --verbose --regex '^p.*d$' /etc",
    "sudo apt  install attr", #testing debconf
    "echo 'test' > test.txt",
    "setfattr -n user.comment -v 'this is a comment' test.txt", #testing libattr1
    "getfattr test.txt",
    "sudo add-shell other_shell", #testing debianutils
    "sudo remove-shell other_shell", #testing debianutils
    "tempfile -d ~/Desktop -n ~/Desktop/tempFILE.txt", #testing debianutils
    "tempfile -n ~/Desktop/tempFILE.txt", #testing debianutils
    "tempfile -d ~/Desktop", #testing debianutils
    "rm ~/Desktop/file*",
    "rm ~/Desktop/tempFILE.txt",
    "ischroot", #testing debianutils
    "sudo ischroot", #testing debianutils
    "savelog -t -u lind ~/Desktop/logfile", #testing debianutils
    "rm ~/Desktop/logfile",
    "rm ~/Desktop/logfile.0",
    "logger -f ~/Desktop/INFO.txt", #testing bsdutils
    "ps -aux", #testing procps
    "cat ~/Desktop/otherRandomTextFile.txt | grep 'hello'", #testing grep
    "ls ~/Desktop | xargs cat",
    "test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )",
    "cron -V",
    "whoami",
    "sudo whoami",
    "rm ~/Desktop/tempFile.txt",
    "rmdir -ry ~/Desktop/gpgTest",
    "mkdir ~/Desktop/gpgTest", #using mkdir to test coreutils
    "cd ~/Desktop/gpgTest",
    "wget https://launchpad.net/veracrypt/trunk/1.24-update7/+download/veracrypt-console-1.24-Update7-Ubuntu-20.04-amd64.deb",
    "wget https://www.idrix.fr/VeraCrypt/VeraCrypt_PGP_public_key.asc",
    "gpg --show-keys VeraCrypt_PGP_public_key.asc", #testing libgpg-error0
    "gpg --with-fingerprint VeraCrypt_PGP_public_key.asc",
    "gpg --import VeraCrypt_PGP_public_key.asc",
    "gpg --verify VeraCrypt_PGP_public_key.asc veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb",
    "gpg --verify veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb.sig veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb"
    "gpgv veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb.sig veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb", #testing gpgv
    "echo 'test' > ~/Desktop/gpg_test.txt",
    "gpg --encrypt file.txt",
    "gpg --dencrypt file.txt.gpg",
    "cat /etc/profile", #testing base-files
    "logger `who`",
    "logger `pwd`",
    "tail -3 /var/log/syslog",
    "hostname", #testing hostname
    "domainname",
    "nodename",
    "dnsdomainname",
    "nisdomainname",
    "ypdomainname",
    "pidof firefox",
    "last",
    "sudo lastb",
    "last -n 5",
    "gcc ~/Desktop/testfile.c",
    "~/Desktop/a.out",
    "gcc ~/Desktop/testfile.c -o ~/Desktop/output.exe",
    "~/Desktop/output.exe",
    "cat ~/Desktop/testfile.c",
    "cat ~/Desktop/otherRandomTextFile.txt | grep 'hello'", #testing grep
    "ps -aux | grep 'firefox'", #testing grep and procps
    "free",
    "free -hl -c 3",
    "sysctl -a --pattern forward",
    "uptime",
    "pmap -XX 1100",
    "vmstat -a",
    "vmstat -f",
    "vmstat -m",
    "vmstat -n",
    "vmstat -s",
    "vmstat -D",
    "vmstat -t",
    "w",
    "git clone https://github.com/util-linux/util-linux.git",
    "cd util-linux",
    "./autogen.sh && ./configure && make",
    "make check-programs",
    "./tests/run.sh",
    "echo 'VERBOSE=1' > ~/Desktop/test_config.conf",
    "sudo ucf ~/Desktop/test_config.conf /etc/ucf.conf", # testing ucf
    "cd ~",
    "find / test.txt", #testing find
    "sudo apt install mlocate", #testing debconf
    "locate test.txt", #testing find
    "gcc {} -o script".format(script2), #testing libstdc++6 and libc6
    "./script", #testing libstdc++6 and libc6
    "sestatus",
    "grep selinux /var/log/audit/audit.log", #testing grep and libsepol1
    "sudo selinux-config-enforcing",
    "SELINUXTYPE=mls",
    "sudo setenforce 0",
    "sudo setenforce 1",
    "logsave -asv ./temp_log ls", #testing e2fsprogs
    "logsave -asv ./temp_log pwd",
    "ping google.com -c 10", #here through the bottom of array for netbase
    "ping 8.8.8.8 -c 10",
    "curl google.com",
    "curl -X POST 'google.com'",
    "wget http://localhost:8080/index.html",
    "nc -G 5 -z 125.0.0.1 20-80",
    "nc -G 5 -z 8.8.8.8 80",
    "netstat -rlv",
    "curl https://www.thrysoee.dk/editline/libedit-20210910-3.1.tar.gz -o ./editline",
    "./editline/configure",
    "cd ./editline",
    "make",
    "sudo make install",
    "cd ..",
    "~/editline/examples/fileman", # testing libedit -- THESE AREN'T AUTOMATED
    "~/editline/examples/tc1",
    "~/editline/examples/wtc1",
]

#need to do a failed login and su for libpam-runtime and util-linux and login
# do a script command for util-linux and bsdutils
# do a command that does gpgv
# watch ls command to test procps
# do a man command
# run make menuconfig on the kernel file to get ncurses to hit
# do one manual apt to hit debconf
# make menuconfig to do the ncurses thing... I just need to get that file window up
# sudo login lind2 -- need to run independently to test libpam-modules and libpam0g and util-linux and login
# sudo passwd lind2 -- to test base-passwd
# sudo login wrong_user
# Also need to gpg gen key, encrypt, decrypt
#   gpg --gen-key
#   gpg --encrypt --recipient 'Your Name' foo.txt
#   gpg --output foo.txt --decrypt foo.txt.gpg



# if input("Would you like to run selinux install commands (Y/N)") == "Y":
#     commands = selinux_install

for command in commands:
    print("\n\n\nCOMMAND::\n" + command + "\n\n\n")
    os.system(command)
    time.sleep(2)
