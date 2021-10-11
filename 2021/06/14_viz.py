import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': [i for i in range(8)],
                   'D': [i**2 for i in range(8)]})

print(df)

# Можно взять и нарисовать фрейм
ax = df.plot()
ax.set_xlabel('x label')
ax.set_ylabel('y label')

print("=================")

# А потом посчитать агрегаты
aggr = df.groupby('A').sum()
print(aggr)

# И их тоже нарисовать
ax2 = aggr.plot(kind='bar')

plt.show()
