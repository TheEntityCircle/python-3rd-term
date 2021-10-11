import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [i ** 2  for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)
print(df)

# Внимание! Сама идея использовать .apply() довольно плохая. Потому что это плохо для производительности.
# Лучше использовать нативные методы.
# Но если очень нужно, то так можно.
print("=================")
print(df.loc[:,['A', 'C', 'D']].apply(lambda x: x**2))
