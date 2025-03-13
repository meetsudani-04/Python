import pandas as pd
a = [2,3,4,5]
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
# p = pd.Series(mydataset)
# q = pd.DataFrame(mydataset)
# print(q)

# df = pd.read_csv('demofiles/demo.csv')
# print(df)

jf = pd.read_json('demofiles/demo.json')
print(jf.to_string())

