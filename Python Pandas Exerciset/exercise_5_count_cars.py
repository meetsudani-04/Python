import pandas as pd
df = pd.read_csv("demofiles/Automobile_data.csv")
company_counts = df["company"].value_counts()
print(company_counts)