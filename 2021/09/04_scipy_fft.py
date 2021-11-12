import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

T = 1.0 / 800.0
N = 600

x = np.linspace(0.0, N * T, N)

# Простая функция
y = np.sin(1 * 2.0 * np.pi * x)

# Сложная функция плюс шум
# rng = np.random.default_rng()
# y_noise = rng.normal(size = x.size)
# y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x) + y_noise

# Посмотрим на саму функцию
plt.plot(x, y)
plt.show()

# Получим Фурье и посмотрим спектр
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.show()