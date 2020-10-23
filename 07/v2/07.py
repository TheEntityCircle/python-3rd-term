from collections import defaultdict

buckets = defaultdict(list)

n = int(input())
for i in range(n):
    ts, id, val = input().split()
    buckets[id].append((int(ts), int(val)))

log = list()
for id, data in buckets.items():
    cur_val = None
    for record in sorted(data, key=lambda e: e[0]):
        if cur_val is None or cur_val != record[1]:
            log.append((record[0], id, record[1]))
            cur_val = record[1]

for r in sorted(log, key=lambda e: (e[0], e[1])):
    print(*r)