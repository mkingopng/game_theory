import nashpy as nash
import numpy as np

row = np.array([[-3, 0], [-5, -1]])
column = np.array([[-3, -5], [0, -1]])
prisoners_dilemma = nash.Game(row, column)
print(prisoners_dilemma)
equilibria = prisoners_dilemma.support_enumeration()
for eq in equilibria:
    print(f"The unique Nash equilibrium is {eq}")

