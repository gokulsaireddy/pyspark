import json

json_filename = "2015-01-01-15.json"

with open(json_filename, 'rb') as f:
    data = json.loads(f)

print(data)
