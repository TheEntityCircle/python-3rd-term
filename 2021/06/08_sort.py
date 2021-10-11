import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [42 * i  for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)
print(df)

# Отсортировать фрейм по колонке можно примерно так
print("=================")
print(df.sort_values(by='D', ascending=False))

# Сортировать фрейм можно и после каких-то ещё операций над ним,
# соединяя их в логические цепочки
print("=================")
print(df.loc[df['D'] > 42].sort_values(by='D', ascending=True))
