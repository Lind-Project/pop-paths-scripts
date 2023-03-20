import os
import json
directory = r'C:\Users\jkoer\Desktop\Cooper\lind_cont\diff-5.15\\'
result = ""
with open (r'C:\Users\jkoer\Desktop\Cooper\lind_cont\final_dict_515.json', 'r') as file:
    final_dict  = json.load(file)

with open('final_dict_readable.txt', 'w') as f: 
    for key, values in final_dict.items():
        f.write(f"{key}:\n")
        for value in values:
            f.write(f"- {value}\n")
