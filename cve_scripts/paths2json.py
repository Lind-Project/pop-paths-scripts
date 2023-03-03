import sys, getopt, os, json

#this is just a temporary path name, just uncomment the line below to use a command line argument for the pathname or hardcode a pathname to the variable pathname before running
#pathname = sys.argv[1]
#pathname =
filename = os.path.basename(pathname)

path_lines = {}
result = ""
with open(filename) as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line.startswith("SF"):
            components = stripped_line.split("/")
            if "include" in components:
                ind = components.index("include")
            elif "mm" in components:
                ind = components.index("mm")
            elif "drm" in components:
                ind = components.index("drm")
            elif "kernel" in components:
                ind = components.index("kernel")
            elif "fs" in components:
                ind = components.index("fs")
            elif "sound" in components:
                ind = components.index("sound")
            elif "lib" in components:
                ind = components.index("lib")
            elif "crypto" in components:
                ind = components.index("crypto")
            elif "net" in components:
                ind = components.index("net")
            elif "security" in components:
                ind = components.index("security")
            elif "drivers" in components:
                ind = components.index("drivers")
            elif "arch" in components:
                ind = components.index("arch")
            elif "block" in components:
                ind = components.index("block")
            elif "ipc" in components:
                ind = components.index("ipc")
            result = "/".join(components[ind:])
            path_lines[result] = []
        elif stripped_line.isdigit():
            line_number = int(stripped_line)
            path_lines[result].append(line_number)

with open("path_lines.json", "w") as f:
    json.dump(path_lines, f)
