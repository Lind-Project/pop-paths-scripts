import sys
f=open(sys.argv[1], 'r') 
line=f.readlines()[0] 
print(line[:line.index(':')])