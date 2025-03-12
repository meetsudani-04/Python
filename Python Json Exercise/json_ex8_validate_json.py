import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError:
        return False
    return True

JsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(JsonData)

print("Given JSON string is Valid", isValid)