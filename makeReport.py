#Author: Tristan Brigham (TristanB22) 
# to reset gcov values: "echo 0>/proc/gcov/vmlinux
import os
import sys
import time


os.system("python ./fuzz.py")


os.system("sudo lcov --capture --output-file {}/kernel.info".format(sys.argv[1]))
os.system("genhtml {}/kernel.info".format(sys.argv[1]))
os.system("firefox {}/index.html".format(sys.argv[1]))
