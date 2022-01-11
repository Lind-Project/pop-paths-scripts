#Author: Tristan Brigham (TristanB22) 
import os
import sys
import time


os.system("python ~/Desktop/fuzz.py")


os.system("sudo lcov --capture --output-file {}/kernel.info".format(sys.argv[1]))
os.system("genhtml {}/kernel.info".format(sys.argv[1]))
os.system("firefox {}/index.html".format(sys.argv[1]))
