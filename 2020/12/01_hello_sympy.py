from sympy import symbols

x, y = symbols('x y')

a = x + y + x
print(a)

a -= x
print(a)

a += (5*y + 12)
print(a)
