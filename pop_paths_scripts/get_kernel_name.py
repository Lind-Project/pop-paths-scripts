import subprocess

gcov_name = "gcovkernel' --"

output = subprocess.getoutput("""sudo grub-mkconfig | grep -iE "menuentry 'Ubuntu, with Linux" | awk '{print i++ " : "$1, $2, $3, $4, $5, $6, $7}'""")
print(output)