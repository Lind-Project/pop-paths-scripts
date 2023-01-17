# Popular Paths Data Collector

### Author: Tristan Brigham

This repository contains all of the scripts and information required to collect popular paths data using any kernel version. The entire process of how the script works is detailed below. It is split up into 3 main parts: config, setup, and data collection.

## CONFIG
This process requires the _config.sh_ script to be run. The command takes two arguments: the directory that we should be running the entire process in as well as the link to the kernel that we are going to be using for the run. Make sure that the directory path is an absolute path. The script puts the arguments into text files to be used in the actual data collection program. An example command is below where we are running everything in the _/hdd_ directory and we are using the kernel specified by the link:

```bash config.sh /hdd https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/linux/5.11.0-49.55/linux_5.11.0.orig.tar.gz```

## SETUP
This process installs the packages and programs that are necesary to collecting the data as well as the kernel. It works simultaneously on the client and server side. The server side process is like so:
- download the server which is going to be run in qemu
- resize the server image so that it fits all of the data that we are going to generate
- start running the server image on a screen instance

The client side is like so:
#### app_armor_and_intall_packages.sh 
- sleep for 5 minutes to allow the qemu image to download and get set up
- create the keys for ssh'ing into the qemu image
- move the keys onto the image so that we can ssh without a password
- run scripts to download the necessary packages, turn off app armor on the image, and restart the image
- wait for the image to restart

#### install_kernel_trinity_ltp.sh 
- download and install trinity and ltp
- download the kernel that we are going to custom build with gcov
- configure the kernel so that it runs with gcov
- install the kernel
- turn on SELinux
- wait for the image to restart

## DATA COLLECTION
- clear all of the gcov data from the kernel
- collect gcov data from the kernel using lcov
- run the pop paths on the image
- collect gcov data from the kernel using lcov
- run trinity and ltp for 6 hours each
- collect gcov data from the kernel using lcov
- exfiltrate the data to the directory that was specified by the config file
- delete the image file

The data file will be time stamped and inside there will be 3 files containing the blank reset data, the pop paths data, and the full data. To visualize this in a browser, simply run `genhtml ./kernel.info` when you are in the data directory that you want to visualize and then open the resulting _index.html_ file.