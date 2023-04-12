import os
import json
#Reads final dictionary and outputs in a readable format
with open (r'./final_dict.json', 'r') as file:
    final_dict  = json.load(file)

with open('final_dict_readable.txt', 'w') as f: 
    for key, values in final_dict.items():
        f.write(f"{key}:\n")
        for value in values:
            f.write(f"- {value}\n")
