#Author: Tristan Brigham (TristanB22) 

''' To Run:

1) Run a command that uses sudo (try "sudo ls")
2) In the same bash prompt, once that command is done, run this
    This ensures that the commands in this script has root privileges without you needing to input the password again

'''
apparmor_stop=[
    "sudo systemctl stop apparmor",
    "sudo apt-get remove apparmor -y",
    "sudo reboot now",
]

selinux_install=[
    "sudo apt install policycoreutils selinux-utils selinux-basics",
    "sudo selinux-activate",
    "sudo selinux-config-enforcing"
    "sudo reboot now",
]

import os
import time

script='#!/usr/bin/perl\n use strict;\n use warnings;\n use Filesys::DiskSpace; \n my $dir = "/home";\n my ($fs_type, $fs_desc, $used, $avail, $fused, $favail) = df $dir;\n my $df_free = (($avail) / ($avail+$used)) * 100.0; \n my $out = sprintf("Disk space on $dir == %0.2f" \n,$df_free);\n print $out;'
script2='#include<iostream>\n #include<math.h>\n using namespace std;\n int main(){\n float number, root;\n cout << "Enter number whose root is to be found: ";\n cin >> number;\n root = sqrt(number);\n cout << "Square root of " << number << " is " << root;\n return 0;\n }'

commands = [
    "sudo systemctl start ssh",
    "sudo systemctl stop ssh",
    "bzip2 -zfk -vv --best test_file.txt",
    "bzip2 -t -vv --best test_file.txt.bz2",
    "bzip2 -df -vv --fast test_file.txt.bz2",
    "blkid -gksu raid --output full -S 1000",
    "echo 'this is a tempfile' > ~/Desktop/tempFile.txt",
    "vim -c 'q' ~/Desktop/tempFile.txt",
    "sudo adduser --disabled-password --gecos '' lind2",
    "sudo passwd lind2",
    "sudo userdel lind2",
    "dir ~/Desktop",
    "cp ./test_file.txt ./test2.txt",
    "mkdir ./temp_dir",
    "rmdir ./temp_dir",
    "printenv",
    "sleep 3",
    "pwd",
    "whoami",
    "who",
    "ln -s file2.txt file3.txt",
    "ls -l file3.txt",
    "uuidgen -t",
    "uuidgen -r",
    "echo 'ls -ahl' > ./script.sh",
    "sudo debconf -p medium --frontend=readline sh -x ./script.sh",
    "chmod u-rw ./test2.txt",
    "chmod a=rwx ./test2.txt",
    "bash -c 'echo helloThere'",
    "bash -i 'echo helloThere'",
    "sudo apt-get -y install cpp-8",
    "sudo apt-get -y remove cpp-8",
    "tar -zcvf ~/Desktop/tarred_information.tar.gz ~/Desktop/fuzzing"
    "cat 'hellohellohellohellohello\n this is linux and I really like the operating system\nit is just interesting that it is taking so long to fuzz it' > ~/Desktop/info.txt",
    "sed 's/linux/unix' ~/Desktop/info.txt",
    "sed 's/hello/aloha/2' ~/Desktop/info.txt",
    "md5sum ~/Desktop/info.txt",
    "cksum ~/Desktop/info.txt",
    "time cat ~/Desktop/info.txt",
    "time ls",
    "time pwd",
    'echo {} > script.pl'.format(script),
    "chmod +x script.pl",
    "./script.pl",
    "echo 'Welcome To The Lind Zone' | sed 's/\([A-Z]\)/\(\1\)/g'",
    "printenv",
    "pwd",
    "ls",
    "sudo apt install lsb-core",
    "lsb_release -a",
    "which pwd",
    "which cat",
    "which ls",
    "mktemp -u",
    "mktemp -d",
    "mktemp",
    "savelog -Cdt ./log_file",
    "run-parts --list --verbose --regex '^p.*d$' /etc",
    "sudo apt  install attr",
    "echo 'test' > test.txt",
    "setfattr -n user.comment -v 'this is a comment' test.txt",
    "getfattr test.txt",
    "sudo add-shell other_shell",
    "sudo remove-shell other_shell",
    "tempfile -d ~/Desktop -n ~/Desktop/tempFILE.txt",
    "tempfile -n ~/Desktop/tempFILE.txt",
    "tempfile -d ~/Desktop",
    "rm ~/Desktop/file*",
    "rm ~/Desktop/tempFILE.txt",
    "ischroot",
    "sudo ischroot",
    "savelog -t -u lind ~/Desktop/logfile",
    "rm ~/Desktop/logfile",
    "rm ~/Desktop/logfile.0",
    "logger -f ~/Desktop/INFO.txt",
    "ps -aux",
    "cat ~/Desktop/otherRandomTextFile.txt | grep 'hello'",
    "ls ~/Desktop | xargs cat",
    "test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )",
    "cron -V",
    "whoami",
    "sudo whoami",
    "rm ~/Desktop/tempFile.txt",
    "rmdir -ry ~/Desktop/gpgTest",
    "mkdir ~/Desktop/gpgTest",
    "cd ~/Desktop/gpgTest",
    "wget https://launchpad.net/veracrypt/trunk/1.24-update7/+download/veracrypt-console-1.24-Update7-Ubuntu-20.04-amd64.deb",
    "wget https://www.idrix.fr/VeraCrypt/VeraCrypt_PGP_public_key.asc",
    "gpg --show-keys VeraCrypt_PGP_public_key.asc"
    "gpg --with-fingerprint VeraCrypt_PGP_public_key.asc",
    "gpg --import VeraCrypt_PGP_public_key.asc",
    "gpg --verify VeraCrypt_PGP_public_key.asc veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb",
    "logger `who`",
    "logger `pwd`",
    "tail -3 /var/log/syslog",
    "hostname",
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
    "cat ~/Desktop/otherRandomTextFile.txt | grep 'hello'",
    "ps -aux | grep 'firefox'",
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
    "cd ~",
    "find / test.txt",
    "sudo apt install mlocate",
    "locate test.txt",
    "echo {} > script.c".format(script2),
    "gcc script.c -o script",
    "./script",
    "sestatus",
    "grep selinux /var/log/audit/audit.log",
    "sudo selinux-config-enforcing",
    "SELINUXTYPE=mls",
    "sudo setenforce 0",
    "sudo setenforce 1",
    "logsave -asv ./temp_log ls",
    "logsave -asv ./temp_log pwd",
    "ping google.com -c 10",
    "ping 8.8.8.8 -c 10",
    "curl google.com",
    "curl -X POST 'google.com'",
    "wget http://localhost:8080/index.html",
    "nc -G 5 -z 125.0.0.1 20-80",
    "nc -G 5 -z 8.8.8.8 80",
    "netstat -rlv",
]

# watch ls command
# do a man command
# make menuconfig to do the ncurses thing
# sudo login lind2 -- need to run independently
# Also need to gpg gen key, encrypt, decrypt
#   gpg --gen-key
#   gpg --encrypt --recipient 'Your Name' foo.txt
#   gpg --output foo.txt --decrypt foo.txt.gpg

if input("Would you like to run selinux install commands (Y/N)") == "Y":
    commands = selinux_install

for command in commands:
    print(command + "\n\n\n")
#    time.sleep(2)
    os.system(command)
