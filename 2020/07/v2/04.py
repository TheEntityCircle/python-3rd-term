path = input()
try:
    with open(path, 'r') as f:
        data = f.read()
        for s in data:
            t = s.lower()[0]
            if t >= 'a' and t <= 'm':
                s = str(chr(ord(s) + 13))
            elif t >= 'n' and t <= 'z':
                s = str(chr(ord(s) - 13))
            print(s, end='')
except:
    print("Can not read file")