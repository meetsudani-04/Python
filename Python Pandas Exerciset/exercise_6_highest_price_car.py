# Exercise 6: Find each company’s Higesht price car

import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")
df["price"] = pd.to_numeric(df["price"])
highest_price = df.groupby("company")["price"].max()
print(highest_price)
