import matplotlib.pyplot as plt

x = [2 * i / 100 for i in range(100)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

fig, ax = plt.subplots(1, 3)  # Create a figure and an axes.
ax[0].plot(x, y1, label='linear')  # Plot some data on the axes.
ax[1].plot(x, y2, label='quadratic')  # Plot more data on the axes...
ax[2].plot(x, y3, label='cubic')  # ... and some more.

for _ in ax:
    _.set_xlabel('x label')  # Add an x-label to the axes.
    _.set_ylabel('y label')  # Add a y-label to the axes.
    _.legend()  # Add a legend.
    _.set_title("Smth") # Add title.

plt.show()