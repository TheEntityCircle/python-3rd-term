from scipy import fft
import matplotlib.pyplot as plt
import numpy as np

T = 1.0 / 800.0
N = 600

x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) + np.random.random((N,1)).flatten()

# plt.plot(x, y)
# plt.show()

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.show()
