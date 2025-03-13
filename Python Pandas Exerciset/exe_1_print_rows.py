# Exercise 1: From the given dataset print the first and last five rows
import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")

print(df.head(5))
print()
print(df.tail(5))