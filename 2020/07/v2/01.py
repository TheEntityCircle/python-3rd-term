try:
    a, op, b = input().split(' ')
    if op == '+':
        print(int(a) + int(b))
    elif op == '-':
        print(int(a) - int(b))
    elif op == '*':
        print(int(a) * int(b))
    elif op == '^':
        print(int(a) ** int(b))
    else:
        raise Exception("Unknown operation")
except:
    print("Bad input")