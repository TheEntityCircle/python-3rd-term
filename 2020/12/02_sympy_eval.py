from sympy import symbols

x = symbols('x')

f = x**2 + 5*x + 1
print(f)
print(f.evalf(subs={x: 2}))

print((x + x + x).evalf(subs={x : 1}))
