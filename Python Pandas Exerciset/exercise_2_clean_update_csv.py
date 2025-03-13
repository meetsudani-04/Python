# Exercise 2: Clean the dataset and update the CSV file
import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv",na_values={'price':["?","n.a"]})
print(df)