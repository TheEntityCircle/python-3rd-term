from sympy import symbols, Eq, solve

x = symbols('x')

a = symbols('a')
f2 = x**2 + a * a * x
e2 = Eq(f2, 0)
print(e2)

result2_1 = solve(e2)
for i, root in enumerate(result2_1):
    print(f'Root {i}: {root}')

print("==================")
a0 = 11
result2_2 = solve(e2, x)
for i, root in enumerate(result2_2):
    print(f'Root {i}: {root}')
    print(f'Root {i} computed for a = {a0}: {root.subs({a: a0})}')