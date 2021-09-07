from sympy import symbols, Eq, solve

x = symbols('x')

f = x**2 + 5 * x + 1
e = Eq(f, 1)
print(e)
print(solve(e))

print("==================")

a = symbols('a')
f2 = x**2 + a * a * x
e2 = Eq(f2, 0)
print(e2)
print(solve(e2))
print(solve(e2, x))