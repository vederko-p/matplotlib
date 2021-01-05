
import matplotlib.pyplot as plt
import numpy as np


# The possible way of using plt.show() and plt.draw().
# pyplot.show() blocks the input of additional commands until you manually kill the plot window,
# additional commands may be as some code additional after the pyplot.show()
# In the usage guide 1 you can see the example of pyplot.show() work: AFter simple example many other
# figures are plotting, but before you see them, you need to close the Simple example figure.
# Below you can see the example of plt.draw(). That command doesnt block the execution of additional code.
# As the result you can see the output of code after plt.draw() before you close the First figure window.
# In the matplotlib documentation you can see the "more correct" way of using plt.show() and plt.draw().
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# The title: What is interactive mode?

# First figure
fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes
fig.canvas.set_window_title('First figure')
plt.draw()

# Second figure
fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], c='red')  # Plot some data on the axes
fig.canvas.set_window_title('Second figure')
plt.show()
