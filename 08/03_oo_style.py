import matplotlib.pyplot as plt

x = [2 * i / 100 for i in range(100)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y1, label='linear')  # Plot some data on the axes.
ax.plot(x, y2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, y3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()