# Exercise 7: Find the average mileage of each car making company

import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")
car = df.groupby('company')
mileage = car[['company','average-mileage']].mean()
print(mileage)
