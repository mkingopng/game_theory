import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt


# define the parabola
# the quadratic function, which is y = -x^2 + 2.5x + 6 here
def function(x):
    return -x ** 2 + 2.5 * x + 6


# define the parabola derivative
def deriv(x):
    return derivative(function, x)


# 100 linearly spaced numbers
y = np.linspace(-5, 10, 100)

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.title("A Sad Quadratic Function")
ax.plot(y, function(y), color="red", label="Function")
plt.plot(y, deriv(y), color="blue", label="Derivative")
plt.legend(loc="lower left")
plt.savefig("sad quadratic.png")
plt.show()

