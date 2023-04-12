#!/bin/bash

## CONFIG SCRIPT
# This script takes four command line arguments 
# the first is the directory that we should be running this entire program in (/hdd for example)
# the second is the link to the kernel that we want to run the pop paths on
# the third is the kernel number to scrape CVEs for
# the fourth is the directory to store the patch files in
# rerun this script with new arguments to overwrite the current configuration

if [[ $# -eq 3 ]]; then
  # Define the filename for the configuration file
  CONFIG_FILE="vars.env"

  # Write the environment variables to the configuration file
  echo "export DIRECTORY=$1" >> $CONFIG_FILE
  echo "export KERNEL_LINK=$2" >> $CONFIG_FILE
  echo "export KERNEL_NUMBER=$3" >> $CONFIG_FILE

  echo "Configuration file created successfully. Use 'source $CONFIG_FILE' to load the variables."
else
  echo "Usage: ./config.sh <directory> <kernel_link> <kernel_number>"
fi
