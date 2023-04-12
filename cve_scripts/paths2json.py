import sys, getopt, os, json

pathname = r'/home/jkoe/pop_paths_data.txt'
filename = os.path.basename(pathname)


path_lines = {}
file_paths = {}
prefixes = []
result = ""
with open(filename) as file:
    for line in file:
        stripped_line = line.strip()
        if stripped_line.startswith("SF"):
            components = stripped_line.split("/")
            file_paths[stripped_line] = 1
            for key in file_paths.keys():
                split = key.split('/')
                prefix = split[5]
                if prefix not in prefixes:
                    prefixes.append(prefix)
            for prefix in prefixes:
                if prefix in components:
                    ind = components.index(prefix)
                    break
            result = "/".join(components[ind:])
            path_lines[result] = []
        elif stripped_line.isdigit():
            line_number = int(stripped_line)
            path_lines[result].append(line_number)
with open("./dictionaries/path_lines.json", "w") as f:
    json.dump(path_lines, f)
