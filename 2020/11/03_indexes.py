import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
print(df)
print("=================")
print(df.index)
print("=================")
print(df.loc[0,'A'])

print("=================")
dates = pd.date_range('20200101', periods=6)
df2 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df2)
print("=================")
print(df2.index)
print("=================")
print(df2.loc['20200101','A'])