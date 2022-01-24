"""
https://www.statology.org/gamma-distribution-in-python/
"""
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# define three Gamma distributions
x = np.linspace(0, 40, 100)
y1 = stats.gamma.pdf(x, a=5, scale=3)
y2 = stats.gamma.pdf(x, a=2, scale=5)
y3 = stats.gamma.pdf(x, a=4, scale=2)

# add lines for each distribution
plt.plot(x, y1, label='shape=5, scale=3')
plt.plot(x, y2, label='shape=2, scale=5')
plt.plot(x, y3, label='shape=4, scale=2')

# add legend
plt.legend()

# display plot
plt.show()

# save plot
plt.savefig("gamma_2.png")
