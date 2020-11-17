import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.arange(8),
                   'D': np.random.rand(8)})

print(df)
print("=================")
aggr = df.groupby('A').sum()
print(aggr)

print("=================")

ax = df.plot()
ax.set_xlabel('x label')
ax.set_ylabel('y label')

ax2 = aggr.plot(kind='bar')

plt.show()
