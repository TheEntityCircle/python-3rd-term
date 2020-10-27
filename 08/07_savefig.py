import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [7, 12, 56, 8]

fig, ax = plt.subplots()

ax.plot(x, y)

plt.savefig("test.png")