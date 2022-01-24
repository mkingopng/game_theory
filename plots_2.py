import numpy as np
import matplotlib.pyplot as plt


# define the parabola a quadratic function, which is y = -x^2 + 2.5x + 6:
def function(x):
    return -x**2 + 2.5*x + 6


# define the parabola derivative
def slope(x):
    return -2*x + 2.5


# define the line space for the parabola
x = np.linspace(-5, 5, 100)

# define the key points for calculating the vertex using the standard quadratic structure y = ax^2 + bx + c:
a = -1
b = 2.5
c = 6


# calculate the vertex, the point where the tangent line = 0
def vertex(a, b, c):
    print("Vertex: (", (-b / (2 * a)), ",", (((4 * a * c) - (b * b)) / (4 * a)), ",")


vertex(a, b, c)

# choose the point to plot the tangent line (vertex)
x1 = 1.25
y1 = function(x1)


# define the tangent line y = m*( x - x1) + y1
def line(x, x1, y1):
    return slope(x1)*(x - x1) + y1


# define the x data range for tangent line
xrange = np.linspace(x1-1, x1 + 1, 10)

# plot the figure
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.title("Quadratic Function & Derivative")
plt.plot(x, function(x), label="Function")
plt.scatter(x1, y1, color="C1", s=50)
plt.plot(xrange, line(xrange, x1, y1), "C1--", linewidth=2, label="Derivative")
plt.legend(loc="lower left")
plt.savefig("quadratic_&_tangent.png")
plt.show()
