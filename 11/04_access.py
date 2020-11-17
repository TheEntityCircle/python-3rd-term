import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.1,
                    'B': pd.Timestamp('20200901'),
                    'C': 111,
                    'D': 42 * np.arange(4),
                    'E': 'foo'})

print(df)
print("=================")
print(df[0:2])
print("=================")
print(df['D'])

print("=================")
print(df.loc[1:2])
print("=================")
print(df.loc[1:2,['A', 'D']])
print("=================")
print(df.loc[1,['A']])
print("=================")
print(df.at[1,'A'])

print("=================")
print(df.iloc[1:2])
print("=================")
print(df.iloc[[0,3],[0,3]])
print("=================")
print(df.iloc[1,3])
print("=================")
print(df.iat[1,3])