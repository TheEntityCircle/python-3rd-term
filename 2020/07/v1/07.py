from collections import defaultdict

props = defaultdict(list)

n = int(input())

for i in range(n):
    tokens = input().split()
    if tokens[1] == "SET":
        props[tokens[2]].append((int(tokens[0]), tokens[3]))
    elif tokens[1] == "DELETE":
        props[tokens[2]].append((int(tokens[0]), None))

for prop, data in props.items():
    data.sort(key=lambda e: e[0])

m = int(input())
for i in range(m):
    ts = int(input())
    answer = {}
    for prop, data in props.items():
        val = None
        for _ts, _val in data:
            if _ts >= ts:
                break
            else:
                val = _val
        answer[prop] = val
    for_out = [str(elem[0]) + " : " + str(elem[1]) for elem in sorted(answer.items(), key=lambda i: i[0]) if
               elem[1] is not None]
    if len(for_out) > 0:
        print(", ".join(for_out))
    else:
        print("(none)")