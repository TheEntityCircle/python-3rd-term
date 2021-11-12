from sympy import symbols, Eq, solve

x = symbols('x')

f = x**2 + 5 * x + 1
e = Eq(f, 1)
print(e)

result = solve(e)
for i, root in enumerate(result):
    print(f'Root {i}: {root}')