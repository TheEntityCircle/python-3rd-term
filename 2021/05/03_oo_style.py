import matplotlib.pyplot as plt

# Теперь сделаем ровно то же самое,
# но общаться с mpl будем в ООП-шном стиле

x = [2 * i / 100 for i in range(100)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

# Попросим создать изображение (fig) с одним графиком на ней (ax)
fig, ax = plt.subplots()

# Полученный ax - объект со смыслом "график" (на самом деле "axes" - "оси").
# Построим всё то же самое, вызывая его методы.
ax.plot(x, y1, label='linear')
ax.plot(x, y2, label='quadratic')
ax.plot(x, y3, label='cubic')

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()

plt.show()

# В каком стиле общаться с mpl - дело вкуса.
# Только смешивать код разных стилей не стоит.