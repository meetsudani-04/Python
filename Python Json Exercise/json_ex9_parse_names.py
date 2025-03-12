# Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
import json

sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = json.loads(sampleJson)
d = []
for i in data:
    d.append((i.get('name')))
print(d)
