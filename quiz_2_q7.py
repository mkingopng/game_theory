"""

"""
from sympy import *

# Q = q1 + q2 + q3
# demand is P = 10 - Q
# cost is c = 0

q1, q2, q3 = symbols('q1 q2 q3')
a, b, c = symbols('a, b, c')
c1, c2, c3 = symbols('a, b, c')


# demand function
def p(q1, q2, q3):
    return 10 - q1 - q2 - q3


# cost function
def cost(q, c):
    return c * q


def profit(q1, q2, q3, c):
    return p(q1, q2, q3)*q1 - cost(q1, c)


foc1 = diff(profit(q1, q2, q3, c1), q1)
foc2 = diff(profit(q1, q2, q3, c2), q2)
foc3 = diff(profit(q1, q2, q3, c3), q3)

answer = solve([foc1, foc2, foc3], [q1, q2, q3])

print(answer)
