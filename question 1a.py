"""

"""

import numpy as np
import nashpy as nash

# Dominant strategy question 1a
A = np.array([[4, 2, 3], [5, 2, 2], [3, 3, 4]])  # A is the row player
B = np.array([[4, 6, 1], [5, 6, 3], [3, 4, 2]])  # B is the column player
rps = nash.Game(A, B)
print(rps)
equilibria = rps.support_enumeration()
for eq in equilibria:
    print(eq)
# interpret the result:
