import pandas as pd

df = pd.read_csv("data.csv", index_col='num')

print(df)

print("=================")

print(df.groupby('A').sum())