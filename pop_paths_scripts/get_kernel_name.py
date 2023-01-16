'''

    This program gets all of the kernels that have been installed 
    and retrieves the name of the one that we want to be running.
    The output of this program can be used to update the grub file.

'''

import subprocess

gcov_name = "gcovkernel' --"

output = subprocess.getoutput("""sudo grub-mkconfig | grep -iE "menuentry 'Ubuntu, with Linux" | awk '{print i++ " : "$1, $2, $3, $4, $5, $6, $7}'""")

for line in output.split("\n"):
    if gcov_name in line:
        print('GRUB_DEFAULT="Advanced options for Ubuntu>' + line[line.index("'") + 1 : line.index("'", line.index("'") + 1)] + "\"")