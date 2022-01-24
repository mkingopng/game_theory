"""
https://www.statology.org/gamma-distribution-in-python/
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# define x-axis values
x = np.linspace(0, 40, 100)

# calculate pdf of Gamma distribution for each x-value
y = stats.gamma.pdf(x, a=5, scale=3)

# create plot of Gamma distribution
plt.plot(x, y)

# display plot
plt.show()

# save plot
plt.savefig("gamma.png")
