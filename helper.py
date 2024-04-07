import json
import csv
def write_json(data, filename,encoding="utf-8"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def write_csv(data, filename):
    with open(filename, 'w', newline='',encoding="utf-8") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
