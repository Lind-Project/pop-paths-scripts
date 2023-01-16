# Author: Tristan Brigham (TristanB22) 
# To reset gcov values: "echo 0 > /sys/kernel/debug/gcov/reset'
import os
import sys
import time


os.system("python ./fuzz.py")

# run the lcov capture command
os.system("sudo lcov --capture --output-file {}/kernel.info".format(sys.argv[1]))

# generate the html file so that we can view the data
os.system("genhtml {}/kernel.info".format(sys.argv[1]))

# view the data
# os.system("firefox {}/index.html".format(sys.argv[1]))
