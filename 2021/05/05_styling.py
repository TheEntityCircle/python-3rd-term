import matplotlib.pyplot as plt

x = [2 * i / 10 for i in range(10)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

fig, ax = plt.subplots()
# Немного поэкспериментируем со стилями самих графиков
ax.plot(x, y1, label='linear', marker='o', linestyle='-', color='red', linewidth=1)
ax.plot(x, y2, label='quadratic', marker='v', linestyle='--', color='green', linewidth=1)
ax.plot(x, y3, label='cubic', marker='^', linestyle='-.', color='black', linewidth=1)
ax.legend()

plt.show()