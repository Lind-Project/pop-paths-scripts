#Author: Tristan Brigham (TristanB22) 
import os

list = ["zlib1g", "libacl1", "libbz2-1.0", "libblkid1", "libpam-modules", "dpkg", "tar", "coreutils", "libuuid1", "passwd", "adduser", "debconf", "libpam-runtime", "sed", "perl-base", "libattr1", "debianutils", "lsb-base", "libgpg-error0", "util-linux", "bsdutils", "grep", "base-files", "findutils", "gzip", "libpam0g", "login", "ncurses-bin", "libstdc++6", "ncurses-base", "apt", "gpgv", "hostname", "base-passwd", "libsepol1", "libselinux1", "sysvinit-utils", "libc6", "libss2", "netbase", "readline-common", "bash", "libpopt0", "procps", "ucf", "libpcre3", "e2fsprogs", "mount", "libslang2", "libedit2"]

for item in list:
    os.system("sudo apt-get install {}".format(item))
