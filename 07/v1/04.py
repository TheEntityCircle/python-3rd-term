path = input()
keyword = input().lower()

c = 0
try:
    with open(path, 'r') as f:
        words = f.read().split()
        for w in words:
            if w.lower() == keyword:
                c += 1
    print(c)
except:
    print(0)