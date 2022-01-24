"""

"""
import numpy as np
import nashpy as nash

# # prisoners dilemma example 1
# Joe = np.array([[-8, 0], [-10, -1]])
# Bob = np.array([[-8, -10], [0, -1]])
# prisoners_dilemma = nash.Game(Joe, Bob)
# print(prisoners_dilemma)
#
# # find the Nash equilibrium with Support enumeration
# equilibria = prisoners_dilemma.support_enumeration()
# for eq in equilibria:
#     print(eq)

# output: (array([1., 0.]), array([1., 0.])), so (confess, confess) is the Nash equilibrium

# Game 2
A = np.array([[4, 0], [0, 2]])  # A is the row player
B = np.array([[2, 0], [0, 4]])  # B is the column player
game2 = nash.Game(A, B)
print(game2)

# find the Nash equilibrium with support enumeration
equilibria = game2.support_enumeration()
for eq in equilibria:
    print(eq)

# interpretation:
# line 1: (array([1., 0.]), array([1., 0.])). This is the first Nash equilibrium, player A chooses strategy 1, so does
# player B.

# line 2: (array([0., 1.]), array([0., 1.])). This is the second Nash equilibrium, player A chooses strategy 2, so does
# player B.

# Line 3: (array([0.66666667, 0.33333333]), array([0.33333333, 0.66666667])). Means we have mixed strategies, and the
# probabilities assigned to each strategy are that Player A will play strategy 1 66.67% of the time, and strategy 2
# 33.33% of the time. Player B plays strategy 1 66.67% of the time and strategy two 33.33% of the time.

# calculate utilities
sigma_r = np.array([.67, .33])
sigma_c = np.array([.33, .67])
pd = nash.Game(A, B)
print(pd[sigma_r, sigma_c])

# the output is [1.3266 1.3266].

