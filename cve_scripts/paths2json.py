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
            result = "/".join(components[ind:])
            path_lines[result] = []
        elif stripped_line.isdigit():
            line_number = int(stripped_line)
            path_lines[result].append(line_number)

with open("path_lines.json", "w") as f:
    json.dump(path_lines, f)
