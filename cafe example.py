"""

"""
import numpy as np
import nashpy as nash

# cafe example
A = np.array([[10, 0], [0, 0]])  # A is the row player
B = np.array([[10, 0], [0, 0]])
rps = nash.Game(A, B)
print(rps)
equilibria = rps.support_enumeration()
for eq in equilibria:
    print(eq)

# interesting return from this - "An even number of (2) equilibria was returned. This indicates that the game is
# degenerate. Consider using another algorithm to investigate." correct result though.

