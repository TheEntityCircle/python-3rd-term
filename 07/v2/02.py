x = [float(a) for a in input().split()]
y = [float(a) for a in input().split()]
z = [float(a) for a in input().split()]

count = 0
n = int(input())
for i in range(n):
    c = [float(a) for a in input().split()]
    if c[0] > x[0] and c[0] < x[1] and c[1] > y[0] and c[1] < y[1] and c[2] > z[0] and c[2] < z[1]:
        count += 1
print(count)