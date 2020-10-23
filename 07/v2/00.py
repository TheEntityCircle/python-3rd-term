n = int(input())
data = list()
for i in range(n):
    data.append(input().split())

for e in sorted(data, key=lambda q: int(q[1]), reverse=True):
    print(e[0])