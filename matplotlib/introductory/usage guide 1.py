
import matplotlib.pyplot as plt
import numpy as np


# Simple example
fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes
fig.canvas.set_window_title('Simple example')
plt.show()

# Figure creating
fig = plt.figure()  # an empty figure with no Axes
fig.canvas.set_window_title('Empty figure')

fig, ax = plt.subplots()  # a figure with a single Axes
fig.canvas.set_window_title('Figure with a single Axes')

fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
fig.canvas.set_window_title('Figure with a 2x2 grid of Axes')

plt.show()

# Some Axes methods: axes.Axes.set_xlim(); axes.Axes.set_ylim();
# set_title(); set_xlabel(); set_ylabel()

# All of plotting functions expect numpy.array or numpy.ma.masked_array as input.
# So in is best to converts data to nampy.array objects prior to plotting

# There are essentially two ways to use Matplotlib:

# Explicitly create figures and axes, and call methods on them (the "object-oriented (OO) style")
x = np.linspace(0, 2, 100)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
fig.canvas.set_window_title('OO-style')
plt.show()

# Rely on pyplot to automatically create and manage the figures and axes, and use pyplot functions for plotting
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# It is better to use the pyplot-style in a Jupyter notebook
# and OO-style for non interactive plotting e.g. in PyCharm
