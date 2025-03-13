# Exercise 8: Sort all cars by Price column
import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")
carsDf = df.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf)
