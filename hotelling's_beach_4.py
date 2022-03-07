"""

"""
from scipy.stats import norm
from matplotlib import pyplot
import numpy as np


pyplot.hist(norm.rvs(loc=1, scale=0.5, size=10000), bins=30, alpha=0.5, label='norm_1')
pyplot.hist(norm.rvs(loc=5, scale=0.5, size=10000), bins=30, alpha=0.5, label='norm_2')
pyplot.legend()
pyplot.show()

"""
Clarification: A normal distribution is defined by mean (loc, distribution center) and standard distribution (scale, 
measure of distribution dispersion or width). rvs generates random samples of the desired normal distribution of  size. 
For example next code generates 4 random elements of a normal distribution (mean = 1, SD = 1).
"""

# norm.rvs(loc=1, scale=1, size=4)
# np.array([0.52154255,  1.40873701,  1.55959291, -0.01730568])


