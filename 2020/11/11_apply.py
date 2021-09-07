import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 1.1,
                    'B': pd.Timestamp('20200901'),
                    'C': pd.Series(1, index=list(range(4)), dtype=np.float32),
                    'D': 42 * np.arange(4),
                    'E': 'foo'})

print(df)
# Внимание! Сама идея использовать .apply() довольно плохая. Потому что это плохо для производительности.
# Лучше использовать нативные методы.
# Но если очень нужно, то так можно.
print("=================")
print(df.loc[:,['A', 'C', 'D']].apply(np.cumsum))
print("=================")
print(df.loc[:,['A', 'C', 'D']].apply(np.cumsum, axis=1))
print("=================")
print(df.loc[:,['A', 'C', 'D']].apply(lambda x: x**2))
