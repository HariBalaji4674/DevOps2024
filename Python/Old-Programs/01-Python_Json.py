
import json

with open('sample.json', 'r') as json_data:
    data = json.load(json_data)

print(data)