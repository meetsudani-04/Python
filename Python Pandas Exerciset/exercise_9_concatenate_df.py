# Exercise 9: Concatenate two data frames using the following conditions
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
d1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
d2 = pd.DataFrame.from_dict(japaneseCars)

final = pd.concat([d1, d2], keys=["Germany", "Japan"])
print(final)