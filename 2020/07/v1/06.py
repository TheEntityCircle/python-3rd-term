from collections import defaultdict
variants = defaultdict(set)

for _ in range(int(input())):
    words = input().split()
    for word in words:
        variants[word.lower()].add(word)

data = [(word, len(vs)) for word, vs in variants.items() if len(vs)>2]
for d in sorted(data, key=lambda x: (-x[1], x[0])):
    print(d[0])
