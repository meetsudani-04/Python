# Exercise 5: Access the nested key ‘salary’ from the following JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

x = json.loads(sampleJson)
print(x['company']['employee']['payble']['salary'])