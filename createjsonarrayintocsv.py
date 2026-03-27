import json
import csv
import sys

# Load your data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

if data:
    fieldnames = data[0].keys()
    
    # We use sys.stdout to "write" to the terminal instead of a file
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
    
    print("--- CSV OUTPUT START ---")
    writer.writeheader()
    writer.writerows(data)
    print("--- CSV OUTPUT END ---")