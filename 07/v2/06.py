from collections import Counter

n = int(input())

data = list()
for i in range(n):
    x, y, q = [int(a) for a in input().split()]
    data.append((x, y, q))

c = Counter(data)
items = [k + (c,) for k, c in c.items() if c >= 2 or k[2] >= 10 or k[0]**2 + k[1]**2 < 10000]

for e in sorted(items, key=lambda z: (z[2], z[3], - (z[0]**2 + z[1]**2)), reverse=True):
    print(e[0], e[1], e[2])