import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': [i for i in range(8)],
                   'D': [i**2 for i in range(8)]})

print(df)
print("=================")

# Можно, например, сгруппировать по значениям в столбце A,
# после чего посчитать суммы по каждой группе.
print(df.groupby('A').sum())

# Так тоже можно. Но лучше без .apply всё же.
#print(df.groupby('A').apply(...))
