import json
import csv
import sys

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

if data:
    fieldnames = data[0].keys()
    
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

    print(" --- CSV OUTPUT START --- ")
    
    writer.writeheader()

    writer.writerows(data)

    print(" --- CSV OUTPUT END --- ")
