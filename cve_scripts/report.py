import os
import json
#add path to the final dictionary on your local machine
#with open (r'', 'r') as file:
    final_dict  = json.load(file)

with open('final_dict_readable.txt', 'w') as f: 
    for key, values in final_dict.items():
        f.write(f"{key}:\n")
        for value in values:
            f.write(f"- {value}\n")
