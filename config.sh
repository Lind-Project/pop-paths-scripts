#!/bin/bash

## CONFIG SCRIPT
# This script takes two command line arguments 
# the first is the directory that we should be running this entire program in (/hdd for example)
# the second is the link to the kernel that we want to run the pop paths on
# rerun this script with new arguments to overwrite the current configuration

echo $1 > ./directory.txt

echo $2 > ./kernel_link.txt