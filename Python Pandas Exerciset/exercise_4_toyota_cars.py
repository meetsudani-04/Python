# Exercise 4: Print All Toyota Cars details
import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")
car = df.groupby('company')
model = car.get_group('toyota')
print(model)