import os
import json
#add direcotry path that contains all the patch files
#directory =r''
result = ""
#add path to the other dictionaries
#with open (r'', 'r') as file:
    path_lines = json.load(file)
    
#with open (r'', 'r') as file2:
    cve_dict = json.load(file2)

#This bottom code should be run to get rid of extra new lines at the end of the patch files
# for filename in os.listdir(directory):
#     if filename.endswith('.txt'):
#         # read the file and split the content into lines
#         with open(os.path.join(directory, filename), "r+",encoding='utf-8') as f:
#             lines = f.read().rstrip('\n')
#             f.writelines(lines)
#             f.truncate()

#main parser that will grab the file names and the line numbers
inter_d = {}
start_count = 0
prev_plus = False  # flag to keep track of whether previous line started with a +
count = 0
name = ""
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(directory+filename, encoding='utf-8') as f:
            content = f.read().rstrip('\n')
            #for line in content.splitlines():
            for i, line in enumerate(content.splitlines()):
                if(line.startswith("diff ")):
                    components = line.split("/")
                    if "include" in components:
                        ind = components.index("include")
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
                    elif "mm" in components:
                        ind = components.index("mm")
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
                    result_split = result.split(" ")
                    name = result_split[0]
                    inter_d[name] = []
                elif(line.startswith("@@")):
                    num = line.split(" ")
                    line_num = num[1]
                    line_num_split = num[1].split(",")
                    line_num_split
                    start_count = abs(int(line_num_split[0]))
                    inter_d[name].append(start_count)
                    prev_plus = False  # reset the flag
                elif line.startswith('-	'):
                    prev_plus = False  # reset the flag
                    next_line = content.splitlines()[i+1]
                    if next_line.startswith("+	"):
                        prev_plus = True
                        continue
                    start_count += 1
                    if name in inter_d:
                        inter_d[name].append(start_count)
                    else:
                        inter_d[name] = [start_count]
                elif line.startswith(" 	") or line.startswith("  	"):
                    prev_plus = False  # reset the flag
                    start_count += 1
                    if name in inter_d:
                        inter_d[name].append(start_count)
                    else:
                        inter_d[name] = [start_count]
                elif line.startswith("+	"):
                    if prev_plus:  # if previous line also started with +
                        continue
                    prev_plus = True
                    start_count += 1
                    if name in inter_d:
                        inter_d[name].append(start_count)
                    else:
                        inter_d[name] = [start_count]
                elif line.strip() == '':
                    prev_plus = False
                    start_count += 1
                    if name in inter_d:
                        inter_d[name].append(start_count)
                    else:
                        inter_d[name] = [start_count]
                elif line.strip() == "--" or line.strip() == "cgit":
                    break

#this gets the git hashs and matches it the the file name so this dict can be combined with the cve_dict
inter_d2 = {}
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(directory+filename, encoding='utf-8') as f:
            content = f.read().rstrip('\n')
            for i, line in enumerate(content.splitlines()):
                if(line.startswith("diff ")):
                        components = line.split("/")
                        if "include" in components: 
                            ind = components.index("include")
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
                        elif "mm" in components:
                            ind = components.index("mm")
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
                        result_split = result.split(" ")
                        inter_d2[result_split[0]] = []
                elif (line.startswith("From")):
                    h = line.split(" ")
                    hashs = h[1]
                    if(len(hashs) < 10):
                        continue
                    if result_split[0] in inter_d2:
                        inter_d2[result_split[0]].append(hashs)
                    else:
                        inter_d2[result_split[0]] = [hashs]
#find matching file names between all the patch files and the pop paths data
matching_keys = {}
for key in inter_d2.keys():
    if key in path_lines:
        matching_keys[key] = inter_d2[key]

#some file names didnt have git hashs so excluded those
cleaner_matching_keys = {k: v for k, v in matching_keys.items() if v}

#matched the CVE number from cve_dict to the matches
matches = {}
for key1, value1 in cve_dict.items():
    for key2, value2 in cleaner_matching_keys.items():
        if value1[0] == value2[0]:
            matches[key1] = []
            matches[key1].append(key2)
            break

#since not all CVE numbers are needed, just get the ones that match
common_dict = {}
for key in matches.keys():
    if key in cve_dict10:
        matches[key].append(cve_dict[key])
common_dict = matches

keys_to_find = cleaner_matching_keys.keys()
matching_files_and_line = {k: v for k, v in inter_d.items() if k in keys_to_find}

#loop through all the line nums and add the ones that match between the patch files and the pop paths to a dictionary
matching_final = {}
for key1, value1 in matching_files_and_line.items():
    for key2, value2 in path_lines.items():
        if key1 == key2:
            matching_final[key1] = []
            for val in value1:
                if val in value2:
                    matching_final[key1].append(val)
        else:
            continue

#combine the line number matchings to the main common_dict that has the CVE# as key and a the git hash, blurb, and file name in a list for the values
for key1, value1 in common_dict.items():
    for key2, value2 in matching_final.items():
        if value1[0] == key2:
            common_dict[key1].append(matching_final[key2])

with open("final_dict.json", "w") as f:
    json.dump(common_dict, f)

