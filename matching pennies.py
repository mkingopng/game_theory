"""

"""
import numpy as np
import nashpy

# Matching pennies game
A = np.array([[1, -1], [-1, 1]])
matching_pennies = nash.Game(A)
print(matching_pennies)
equilibria = matching_pennies.support_enumeration()
for eq in equilibria:
    print(eq)
# zero sum game with payoff matices
