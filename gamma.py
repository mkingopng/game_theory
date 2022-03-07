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

# save plot
plt.savefig("gamma.png")

# display plot
plt.show()

params = stats.gamma.fit(y)
print(stats.gamma.mean(*params))

