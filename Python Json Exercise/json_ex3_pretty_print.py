import json
sampleJson = {"key1": "value1", "key2": "value2"}
x = json.dumps(sampleJson,indent=4)
print(x)