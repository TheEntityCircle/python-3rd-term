import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.arange(8),
                   'D': np.random.rand(8)})

print(df)
print("=================")

print(df.groupby('A').sum())
#print(df.groupby('A').apply(...))
