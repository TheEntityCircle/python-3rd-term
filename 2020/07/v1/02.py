z = input()
parts = z.split('.')

if len(parts) == 1:
    print(int(z) - 1)
else:
    i, f = parts
    precision = len(f)
    t = float(z) * 10**precision
    t -= 1
    fmt_str = "%." + str(precision) + "f"
    print(fmt_str % (t / 10**precision))