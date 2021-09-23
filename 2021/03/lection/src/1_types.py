a = 5
b = 5.5
l = list()
d = dict()

print(type(a))
print(type(b))
print(type(l))
print(type(d))

print(isinstance(a, int))
print(isinstance(a, str))
print(isinstance(b, object))

#print(object.__subclasses__())

def classlookup(cls):
    c = list(cls.__bases__) #__bases__ tuple of bases
    for base in c:
        c.extend(classlookup(base))
    return c

print(classlookup(bool))