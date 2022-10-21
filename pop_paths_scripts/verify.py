from doctest import master
import os
import numpy as np
import pandas as pd 

master_directory="~/Desktop/nr_data/nr_pop_paths"
first_string="nr_pop_paths"
second_string="nr_reachable"
third_string="r_reachable"
substring="class=\"headerCovTableEntry\">"
master_array=[]

dir_list = os.walk(master_directory)
error = 0

for folder in dir_list:
    folder_name = folder[0]
    files = folder[2]
    for file in files:
        if file[-10:] == ".gcov.html":
            count = 0
            temp_array = []
            name = folder_name + "/" + file
            temp_array.append(name)
            flag=False
            with open(name, "r") as f:
                contents = f.readlines()
                for line in contents:
                    if substring in line:
                        count = count + 1
                        temp_int = int(line[line.index(">") + 1:-6])
                        if temp_int > 0 and count == 1:
                            flag=True
                        temp_array.append(line[line.index(">") + 1:-6])
            if flag is True:
                try:
                    with open(name.replace(first_string, second_string), "r") as f:
                        contents = f.readlines()
                        for line in contents:
                            if substring in line:
                                count = count + 1
                                temp_array.append(line[line.index(">") + 1:-6])
                        f.close()
                    master_array.append(temp_array)
                except:
                    # temp_array[6:9] = temp_array[1:5]
                    error = error + 1
                    print("MISSING:: {}".format(name.replace(second_string, third_string)))

# print(master_array)
print("ERROR: {}".format(error))
new_arr=[]

for arr in master_array:
    temp_array=[arr[0], arr[1], arr[5], arr[2]]
    new_arr.append(temp_array)

pd.DataFrame(new_arr).to_csv("~/Desktop/data_paths.csv")