n = int(input())

T = 0
Tc = 0
P = 0
Pc = 0
for i in range(n):
    data = [float(a) for a in input().split()]
    T += data[0]
    Tc += 1
    if data[0] >= -70 and data[0] <= 80:
        P += data[1]
        Pc += 1

print("%.4f %.4f" % (T / Tc, P / Pc))