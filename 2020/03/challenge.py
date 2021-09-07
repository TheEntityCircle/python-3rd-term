class MyClass:
    def __init__(self, a=0, b=0, c=0):
        self.a, self.b, self.c = a, b, c

    def __repr__(self):
        return "MyClass instance with values (%d; %d; %d)" % (self.a, self.b, self.c)

    def __hash__(self):
        return hash(self.a)


z = MyClass(1, 2, 3)
q = MyClass(1, 8, 42)

s = set()
s.add(z)
s.add(q)

for v in s:
    print(v)