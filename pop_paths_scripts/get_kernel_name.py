import subprocess

gcov_name = "gcovkernel' --"

output = subprocess.getoutput("""sudo grub-mkconfig | grep -iE "menuentry 'Ubuntu, with Linux" | awk '{print i++ " : "$1, $2, $3, $4, $5, $6, $7}'""")

for line in output.split("\n"):
    if gcov_name in line:
        print('GRUB_DEFAULT="Advanced options for Ubuntu>' + line[line.index("'") + 1 : line.index("'", line.index("'") + 1)] + "\"")