import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [i ** 2  for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)
print(df)

# Можно посчитать от данных какие-нибудь статы

# Кстати, если что-нибудь будет нам многократно нужно,
# его очень даже можно запомнить в какой-нибудь переменной.
target = df.loc[df['D'] > 0, 'D']
print("=================")
print(target)

# Теперь посчитаем статы от выбранного кусочка данных
print("=================")
print(target.min())
print(target.max())
print(target.mean())
print(target.median())

# На правах ремарки. Вот этот результат вряд ли вам понравится.
# print(df.loc[:,['D']].mean())

# Потому что его тип будет не float, а pandas.core.series.Series
# Потому что указали не один столбец, а список из одного столбца.
# print(type(df.loc[:,['D']].mean()))
