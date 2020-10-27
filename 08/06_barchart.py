import matplotlib.pyplot as plt

data = {'alpha': 6, 'bravo': 12, 'charlie': 11, 'donny': 13}

bar_numbers = range(len(data))
labels = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()

ax.bar(bar_numbers, values)
ax.set_xticks(bar_numbers)
ax.set_xticklabels(labels)

plt.show()