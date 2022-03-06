import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 50, 100)

# plot the first function
plt.plot(x,  -0.5*x + 24, '-r', label="Firm 1's best response function")

# plot the second function
plt.plot(x,  -2*x + 48, '-b', label="Firm 2's best response function")

# set the y-axis limits
plt.ylim(top=50, bottom=0)

# set the x-axis limits
plt.xlim(left=0, right=50)

# plot title
plt.title('Cournot Competition', fontsize=20)

# x axis label
plt.xlabel('q₁', fontsize=16, color='#1C2833')

# y axis label
plt.ylabel('q₂', fontsize=16, color='#1C2833')

# legend location
plt.legend(loc='upper right')

# locations to plot text
l1 = np.array((3, 45))
l2 = np.array((22, 14))

# rotation angle
angle1 = 303
angle2 = 340

# plot text
th1 = ax.text(*l1, "Firm 1's best response", fontsize=10, rotation=angle1, rotation_mode='anchor')
th2 = ax.text(*l2, "Firm 2's best response", fontsize=10, rotation=angle2, rotation_mode='anchor')

# include gridlines
plt.grid()

# save the plot as a png file
plt.savefig('Cournot Competition.png')

# show the plot
plt.show()
