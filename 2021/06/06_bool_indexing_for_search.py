import pandas as pd

data = {'A': 1.1,
        'B': pd.Timestamp('20200901'),
        'C': 111,
        'D': [42 * i  for i in range(4)],
        'E': 'foo'}

df = pd.DataFrame(data)
print(df)

# Правильный способ выборки чего-нибудь по критерию
print("=================")
print(df[df['D'] > 0])