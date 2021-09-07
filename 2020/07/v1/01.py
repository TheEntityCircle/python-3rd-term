sum = 0
for z in input().split():
    try:
        sum += int(z)
    except:
        pass
print(sum)