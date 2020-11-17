import pandas as pd

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

print(left)
print("=================")
print(right)
print("=================")
m = pd.merge(left, right, on='key')
print(m)

right2 = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("=================")
print(left)
print("=================")
print(right2)
print("=================")
print(pd.merge(left, right2, on='key'))

left2 = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
print("=================")
print(left2)
print("=================")
print(right2)
print("=================")
print(pd.merge(left2, right2, on='key'))