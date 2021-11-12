import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Функция, которой описываются наши данные
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


# Настоящие значения параметров
real_params = [2.5, 1.3, 0.5]
# Набор точек
xdata = np.linspace(0, 4, 50)
y = func(xdata, *real_params)

# Шум по оси OY в наших точках
rng = np.random.default_rng()
y_noise = 0.2 * rng.normal(size = xdata.size)
ydata = y + y_noise

# Посмотрим на вид функции с шумом
plt.plot(xdata, ydata, 'b-', label='data + noise: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(real_params))

# Попросим определить параметры функции по точкам
params1, _ = curve_fit(func, xdata, ydata)
# Напечатаем и нарисуем результат
print(params1)
plt.plot(xdata, func(xdata, *params1), 'r-', label='unconstrained fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(params1))

# Попросим определить параметры функции по точкам, добавив ограничений на диапазоны значений
params2, _ = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
# Напечатаем и нарисуем этот результат тоже
print(params2)
plt.plot(xdata, func(xdata, *params2), 'g--', label='constrained fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(params2))

plt.legend()
plt.show()