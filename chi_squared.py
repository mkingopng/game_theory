"""
https://www.statology.org/plot-chi-square-distribution-python/
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# x-axis ranges from 0 to 20 with .001 steps
x = np.arange(0, 20, 0.001)

# define multiple Chi-square distributions
plt.plot(x, chi2.pdf(x, df=4), label='df: 4', color='gold')
plt.plot(x, chi2.pdf(x, df=8), label='df: 8', color='red')
plt.plot(x, chi2.pdf(x, df=12), label='df: 12', color='pink')

# add legend to plot
plt.legend(title='Parameters')

# add axes labels and a title
plt.ylabel('Density')
plt.xlabel('x')
plt.title('Chi-Square Distributions', fontsize=14)
plt.show()
plt.savefig("chi_squared.png")
