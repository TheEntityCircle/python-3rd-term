import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.1,
                    'B': pd.Timestamp('20200901'),
                    'C': 111,
                    'D': 42 * np.arange(4),
                    'E': 'foo'})
print(df)
print("=================")
print(df.dtypes)
print("=================")
print(df.index)
print("=================")
print(df.columns)
