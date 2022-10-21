# Author: Tristan Brigham (TristanB22) 
# To reset gcov values: "echo 0 > /sys/kernel/debug/gcov/reset
import os
import sys
import time


os.system("python ./fuzz.py")


os.system("sudo lcov --capture --output-file {}/kernel.info".format(sys.argv[1]))
os.system("genhtml {}/kernel.info".format(sys.argv[1]))
os.system("firefox {}/index.html".format(sys.argv[1]))
