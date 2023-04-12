import os
import json
#Reads final dictionary and outputs in a readable format
with open (r'./dictionaries/final_dict.json', 'r') as file:
    final_dict  = json.load(file)
output_dir = "./output"
if not os.path.exists(output_dir):
    os.makdris(output_dir)
with open('./output/final_dict_readable.txt', 'w') as f: 
    for key, values in final_dict.items():
        f.write(f"{key}:\n")
        for value in values:
            f.write(f"- {value}\n")
