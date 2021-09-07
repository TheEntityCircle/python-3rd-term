import matplotlib.pyplot as plt

x = [2 * i / 100 for i in range(100)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

plt.plot(x, y1, label='linear')
plt.plot(x, y2, label='quadratic')
plt.plot(x, y3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()
