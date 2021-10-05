import matplotlib.pyplot as plt

# Это наши данные
data = {'alpha': 6, 'bravo': 12, 'charlie': 11, 'donny': 13}

# Барчарт строится немного неочевидным образом. Это не самая сильная сторона mpl.

# Это номера столбиков ("координаты по ОХ")
bar_numbers = range(len(data))
# Это подписи столбиков
labels = list(data.keys())
# Это значения столбиков
values = list(data.values())

fig, ax = plt.subplots()

# Сама картинка барчарта строится из номеров столбиков и их значений
ax.bar(bar_numbers, values)
# Потом на оси ОХ задаются положения отсечек с подписями
ax.set_xticks(bar_numbers)
# И текст этих подписей
ax.set_xticklabels(labels)

plt.show()