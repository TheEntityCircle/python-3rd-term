import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi, 100)
y = 42 * np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
plt.show()