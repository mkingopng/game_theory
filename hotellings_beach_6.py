from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.pyplot import axvline
from scipy.stats import skewnorm, rv_histogram

data = skewnorm.rvs(5, loc=100, scale=200, size=1000).astype(int)  # create some random data

ax = sns.distplot(data, kde_kws={'label': 'kde of given data'}, label='histogram')  # draw histogram & kde of data
params = skewnorm.fit(data, 10, loc=80, scale=40)  # parameters to fit a skewnorm to the data
x = np.linspace(0, 1000, 5000)  # draw the pdf of the fitted skewnorm
ax.plot(x, skewnorm.pdf(x, *params), label='approximated skewnorm')  # plot the skewnowm

mean = data.mean()  # calculate the mean of the data
median = np.median(data)  # calculate the median of the data
middle = 500

axvline(x=mean, color='blue')  # set the mean line
axvline(x=median, color='green')  # set the median line
axvline(x=middle, color='black')  # set the middle line

plt.xlabel('Distance')  # set the x-axis label
plt.title('Hotellings Beach')  # set the title

plt.ylim(top=0.004, bottom=0)  # set the y-axis limits
plt.xlim(left=0, right=1000)  # set the x-axis limits

l1 = np.array((mean, 0.0035))  # location to plot mean text
l2 = np.array((median, 0.0034))  # location to plot median text
l3 = np.array((middle, 0.0034))  # location to plot the middle text

angle1 = 90  # rotation angle for text
angle2 = 90  # rotation angle for text
angle3 = 90  # rotation angle for text

th1 = ax.text(*l1, "mean", fontsize=10, color='blue', rotation=angle1, rotation_mode='anchor')  # plot text mean
th2 = ax.text(*l2, "median", fontsize=10, color='green', rotation=angle2, rotation_mode='anchor')  # plot text median
th3 = ax.text(*l3, "middle", fontsize=10, color='black', rotation=angle3, rotation_mode='anchor')

plt.legend()  # set the legend
plt.savefig('Hotellings beach')  # save the figure
plt.show()  # show the figure

print(mean)
print(median)

mean = 258.514
median = 236.0
