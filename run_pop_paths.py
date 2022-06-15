# Author: Tristan Brigham (TristanB22) 

''' To Run:

1) Run a command that uses sudo (try "sudo ls")
2) In the same bash prompt, once that command is done, run this
    This ensures that the commands in this script has root privileges without you needing to input the password again

'''

import os
import time
import sys

apparmor_stop=[ #we need to run this before installing selinux because apparmor and selinux conflict
    "sudo systemctl stop apparmor",
    "sudo apt-get remove apparmor -y",
    "sudo reboot now",
]

selinux_install=[ #the commands for installing and starting selinux
    "sudo apt install policycoreutils selinux-utils selinux-basics",
    "sudo selinux-activate",
    "sudo cp {} /etc/selinux/config".format(os.getcwd()+"/pop-paths-scripts/scripts/selinux-policy"),
    "sudo reboot now",
]

extra_files="extra_files"
mount_file_name="./pop-paths-scripts/{}/mnt_file".format(extra_files) 

bash_script_file=os.getcwd()+"/pop-paths-scripts/scripts/bash_script.sh"
perl_script_file=os.getcwd()+"/pop-paths-scripts/scripts/perl_script"
script2=os.getcwd()+"/pop-paths-scripts/scripts/cscript2.cpp"
c_command_line_args=os.getcwd()+"/pop-paths-scripts/scripts/cscript.c"
function_slang=os.getcwd()+"/pop-paths-scripts/scripts/slang"
python_mount_script=os.getcwd()+"/pop-paths-scripts/scripts/mount.py {}".format(mount_file_name)
print(os.getcwd())

# just using the command line hits libss2

commands = [
    "sudo apt-get install -y libconfig-dev libedit-dev curl libreadline6-dev slsh",
    "sudo adduser --disabled-password --gecos '' lind2", #testing libpam-modules and libpam0g and adduser
    "sudo passwd lind2", #testing passwd and lsb-base
    "sudo userdel lind2",
    "rm -r ~/Desktop/gpgTest",
    "mkdir ~/Desktop/gpgTest", #using mkdir to test coreutils
    "cd ~/Desktop/gpgTest",
    "wget https://old-releases.ubuntu.com/releases/16.04.2/ubuntu-16.04.1-desktop-amd64.iso",
    "wget https://old-releases.ubuntu.com/releases/16.04.2/SHA256SUMS",
    "wget https://old-releases.ubuntu.com/releases/16.04.2/SHA256SUMS.gpg",
    "gpg2 --verify SHA256SUMS.gpg SHA256SUMS",
    "gpg2 --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys FBB75451 EFE21092",
    "gpg2 --verify SHA256SUMS.gpg SHA256SUMS",
    "sha256sum ubuntu-16.04.1-desktop-amd64.iso",
    "wget https://yum.oracle.com/ISOS/OracleLinux/OL8/u6/x86_64/x86_64-boot-uek.iso", #testing libgpg-error0
    "sudo curl https://yum.oracle.com/RPM-GPG-KEY-oracle-ol8 | sudo gpg --import",
    "wget https://linux.oracle.com/security/gpg/checksum/OracleLinux-R8-U6-Server-x86_64.checksum",
    "sudo gpg --verify-files OracleLinux-R8-U6-Server-x86_64.checksum",
    "gpg --with-fingerprint VeraCrypt_PGP_public_key.asc",
    "sudo curl https://yum.oracle.com/RPM-GPG-KEY-oracle-ol8 -o RPM-GPG-KEY-oracle",
    "gpg --quiet --keyid-format 0xlong --with-fingerprint RPM-GPG-KEY-oracle",
    "grep x86_64-boot-uek.iso OracleLinux-R8-U6-Server-x86_64.checksum | sha256sum -c",
    "cd /home/purple/Desktop",
    "sudo curl https://www.thrysoee.dk/editline/libedit-20210910-3.1.tar.gz --output ./editline",
    "tar -xvf editline",
    "cd ./libedit-20210910-3.1",
    "./configure",
    "make",
    "sudo make install",
    "cd /home/purple/Desktop",
    "/home/purple/Desktop/libedit-20210910-3.1/examples/fileman", # testing libedit2 -- THESE AREN'T AUTOMATED
    "/home/purple/Desktop/libedit-20210910-3.1/examples/tc1",
    "/home/purple/Desktop/libedit-20210910-3.1/examples/wtc1",
    "echo 'test' > /home/purple/Desktop/gpg_test.txt", #testing gpg -- ALSO NOT AUTOMATED
    "gpg -r purple --encrypt /home/purple/Desktop/gpg_test.txt",
    "gpg --decrypt /home/purple/Desktop/gpg_test.txt.gpg",
    "curl https://www.jedsoft.org/fun/complex/fztopng/fztopng -o ./fztopng", #getting script for libslang2
    "sudo chmod +x fztopng",
    "sudo ./fztopng -x -8:8:#512 -y -2:2:#128 -o sin_hsv.png -f 'sin(z)'", #testing libslang2
    "sudo ./fztopng -x -8:8:#512 -y -2:2:#128 -o sin_hsv.png {}".format(function_slang),
    "cp /usr/share/common-licenses/GPL-3 ./{}".format(extra_files), #testing libpcre3
    "grep '^GNU' /usr/share/common-licenses/GPL-3",
    "grep '^[A-Z]' /usr/share/common-licenses/GPL-3",
    "grep '([A-Za-z ]*)' /usr/share/common-licenses/GPL-3",
    "grep -E '(GPL|General Public License)' /usr/share/common-licenses/GPL-3",
    "grep -E '[[:alpha:]]{16,20}' /usr/share/common-licenses/GPL-3",
    "gcc -o ./ex {}".format(c_command_line_args), #testing libpopt0 (command line arguments) and libc6
    "./ex 'hello'",
    "sudo dd if=/dev/zero of=loopbackfile.img bs=1M count=10", #testing mount for the next several lines
    "sudo losetup -f loopbackfile.img",
    "sudo losetup -a | grep 'loopbackfile.img' > '{}'".format(mount_file_name),
    "sudo mkfs.ext4 $(python {})".format(python_mount_script),
    "sudo mkdir /media/loop100",
    "sudo mount $(python {}) /media/loop100".format(python_mount_script),
    "sudo umount /media/loop100",
    "sudo losetup -d $(python {})".format(python_mount_script),
    "sudo rm loopbackfile.img",
    "echo 'hello' > test_file.txt",
    "bzip2 -zfk -vv --best test_file.txt", #zipping files to test libbz2-1.0
    "bzip2 -t -vv --best test_file.txt.bz2",
    "bzip2 -df -vv --fast test_file.txt.bz2",
    "blkid -gksu raid --output full -S 1000", #using blkid command to test libblkid1
    "echo 'this is a tempfile' > /home/purple/Desktop/tempFile.txt",
    "cat /home/purple/Desktop/tempFile.txt | wall", #testing bsdutils
    "vim -c 'q' /home/purple/Desktop/tempFile.txt",
    "dir /home/purple/Desktop",
    "cp /home/purple/Desktop/test_file.txt /home/purple/Desktop/test2.txt",
    "mkdir ./temp_dir", 
    "rmdir ./temp_dir", #using rmdir to test coreutils
    "printenv",
    "sleep 3",
    "pwd", #testing lsb-base
    "ps -aux", #testing procps
    "last", #testing sysvinit-utils
    "sudo lastb", #testing sysvinit-utils
    "mesg y", 
    "mesg n",
    "kill 100000", #testing util-linux
    "whoami",
    "id", #testing lsb-base
    "who",
    "ln -s file2.txt file3.txt",
    "ls -l file3.txt",
    "uuidgen -t", #testing libuuid1 and util-linux
    "uuidgen -r",
    "sudo touch ./script.sh",
    "echo 'ls -ahl' > ./script.sh",
    "sudo debconf -p medium --frontend=readline sh -x ./script.sh",
    "sudo chmod u-rw ./test2.txt", #using chmod command to test libacl
    "sudo chmod a=rwx ./test2.txt",
    "bash -c 'echo helloThere'",
    "sudo apt-get -y install cpp-8",  #using apt command to test dpkg and apt
    "sudo apt-get -y remove cpp-8",
    "tar -zcvf /home/purple/Desktop/tarred_information.tar.gz /home/purple/Desktop/fuzzing", #using tar gz to test zlib1g and tar and gzip
    "cat 'hellohellohellohellohello\n this is linux and I really like the operating system\nit is just interesting that it is taking so long to fuzz it' > /home/purple/Desktop/info.txt", #testing lsb-base
    "sed 's/linux/unix' /home/purple/Desktop/info.txt", #testing sed
    "sed 's/hello/aloha/2' /home/purple/Desktop/info.txt",
    "md5sum /home/purple/Desktop/info.txt",
    "cksum /home/purple/Desktop/info.txt",
    "time cat /home/purple/Desktop/info.txt",
    "time ls",
    "time pwd",
    "sudo chmod +xrw {}".format(bash_script_file), #testing bash
    "bash {}".format(bash_script_file),
    "sudo chmod +x {}".format(perl_script_file),#testing perl-base
    "{}".format(perl_script_file),
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
    "tempfile -d /home/purple/Desktop -n /home/purple/Desktop/tempFILE.txt", #testing debianutils
    "tempfile -n /home/purple/Desktop/tempFILE.txt", #testing debianutils
    "tempfile -d /home/purple/Desktop", #testing debianutils
    "rm /home/purple/Desktop/file*",
    "rm /home/purple/Desktop/tempFILE.txt",
    "ischroot", #testing debianutils
    "sudo ischroot", #testing debianutils
    "savelog -t -u lind /home/purple/Desktop/logfile", #testing debianutils
    "rm /home/purple/Desktop/logfile",
    "rm /home/purple/Desktop/logfile.0",
    "logger -f /home/purple/Desktop/INFO.txt", #testing bsdutils
    "ps -aux", #testing procps
    "cat /home/purple/Desktop/otherRandomTextFile.txt | grep 'hello'", #testing grep
    "ls /home/purple/Desktop | xargs cat",
    "test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )",
    "sudo cron", 
    "whoami",
    "sudo whoami",
    "rm /home/purple/Desktop/tempFile.txt",
    "cat /etc/profile", #testing base-files
    "logger `who`",
    "logger `pwd`",
    "tail -3 /var/log/syslog",
    "hostname", #testing hostname
    "domainname",
    "dnsdomainname",
    "nisdomainname",
    "ypdomainname",
    "pidof firefox", #testing sysvinit-utils
    "last",
    "sudo lastb",
    "last -n 5",
    "cat /home/purple/Desktop/otherRandomTextFile.txt | grep 'hello'", #testing grep
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
    "/home/purple/Desktop/util-linux/autogen.sh",
    "/home/purple/Desktop/util-linux/configure",
    "make",
    "make check-programs",
    "./tests/run.sh",
    "echo 'VERBOSE=1' > /home/purple/Desktop/test_config.conf",
    "sudo ucf /home/purple/Desktop/test_config.conf /etc/ucf.conf", # testing ucf
    "cd /home/purple",
    "find / test.txt", #testing findutils
    "sudo apt install mlocate", #testing debconf
    "locate test.txt", #testing findutils
    "gcc {} -o script".format(script2), #testing libstdc++6 
    "./script", #testing libstdc++6 
    "sestatus",
    "sudo selinux-activate", #testing libsepol1 and libselinux1
    "grep selinux /var/log/audit/audit.log", #testing grep
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

    # Cleaning up
    "sudo rm -fr /home/purple/Desktop/util-linux",
]

### MANUAL COMMANDS ###

# do a script command for util-linux and bsdutils
# watch ls command to test procps
# do a man command to test readline-common
# run make menuconfig on the kernel file to get ncurses-bin to hit
# do one manual apt to hit debconf
# sudo login lind2 -- need to run independently to test libpam-modules and libpam0g and util-linux and login
# sudo passwd lind2 -- to test base-passwd
# sudo login wrong_user -- for libpam-runtime and util-linux and login
# Also need to gpg gen key, encrypt, decrypt
#   gpg --gen-key
#   gpg --export -a **EMAIL**
#   gpg --no-default-keyring --keyring ~/.gnupg/trustedkeys.kbx --import
#   echo hello world | gpg -s -u **EMAIL** | gpgv


count=0
try:
    count = int(sys.argv[1])
except:
    pass

for i, command in enumerate(commands[count:]):
    print("\n\n\nCOMMAND {}::\n".format(i + count) + command + "\n\n\n")
    os.system(command)
    time.sleep(.3)
