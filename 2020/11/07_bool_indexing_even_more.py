import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.1,
                    'B': pd.Timestamp('20200901'),
                    'C': pd.Series(1, index=list(range(4)), dtype=np.float32),
                    'D': 42 * np.arange(4),
                    'E': 'foo'})
print(df)
print("=================")
print(df['D'] > 42)
print("=================")
print(df[df['D'] > 42])
print("=================")
print(df[df['D'] > 42].loc[:,'D'])
# так нельзя! потому что цепочка df[].loc[] смотрит уже в копию
# print("=================")
# df[df['D'] > 42].loc[:,'D'] = 0
print("=================")
print(df.loc[df['D'] > 42,['A','D']])
print("=================")
# а так можно! потому что df.loc[] смотрит в реальные данные
df.loc[df['D'] > 42,'D'] = 0
print(df)
