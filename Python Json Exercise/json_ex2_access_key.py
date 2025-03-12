import json
data = """{"key1" : "value1", "key2" : "value2"}"""
x = json.loads(data)
print(x['key2'])