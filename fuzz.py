#Author: Tristan Brigham (TristanB22) 
import os
import time

commands = ["sudo systemctl start ssh",
"man ls",
"man chmod",
"echo 'this is a tempfile' > ~/Desktop/tempFile.txt",
"vim ~/Desktop/tempFile.txt",
"sudo adduser lind2",
#"sudo passwd lind2",
"sudo login lind2",
"sudo userdel lind2",
"bash -c 'echo helloThere'",
"bash -i 'echo helloThere'",
"sudo apt-get -y install cpp-8",
"sudo apt-get -y remove cpp-8",
"tar -zcvf ~/Desktop/tarred_information.tar.gz ~/Desktop/fuzzing"
"cat 'hellohellohellohellohello
this is linux and I really like the operating system
it is just interesting that it is taking so long to fuzz it' > ~/Desktop/info.txt",
"sed 's/linux/unix' ~/Desktop/info.txt",
"sed 's/hello/aloha/2' ~/Desktop/info.txt",
"echo 'Welcome To The Lind Zone' | sed 's/\([A-Z]\)/\(\1\)/g'",
"printenv",
"pwd",
"ls",
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
# "cat ~/Desktop/otherRandomTextFile.txt | grep -r '*'",
# "ls *temp* | xargs wc",
# "ls ~/Desktop | xargs cat",
"test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )",
"cron -V",
"whoami",
"sudo whoami",
"rm ~/Desktop/tempFile.txt",
"rmdir -ry ~/Desktop/gpgTest",
"mkdir ~/Desktop/gpgTest",
"cd ~/Desktop/gpgTest",
"wget https://launchpad.net/veracrypt/trunk/1.24-update7/+download/veracrypt-console-1.24-Update7-Ubuntu-20.04-amd64.deb",
"wget https://www.idrix.fr/VeraCrypt/VeraCrypt_PGP_public_key.asc
gpg --show-keys VeraCrypt_PGP_public_key.asc
gpg --with-fingerprint VeraCrypt_PGP_public_key.asc",
"gpg --import VeraCrypt_PGP_public_key.asc",
"gpg --verify VeraCrypt_PGP_public_key.asc veracrypt-1.24-Update7-Ubuntu-20.04-amd64.deb",
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
#"watch ls",
#"watch ps -aux",
#"watch 'sudo systemctl start ssh'",
#"watch 'sudo systemctl stop ssh'"
]

for command in commands:
    print(command + "







")
#    time.sleep(2)
    os.system(command)
