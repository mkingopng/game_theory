import nashpy as nash
import numpy as np

row = np.array([[10, 0], [0, 0]])
column = np.array([[10, 0], [0, 0]])
meeting_game = nash.Game(row, column)
print(meeting_game)
equilibria = meeting_game.support_enumeration()
for eq in equilibria:
    print(f"The unique Nash equilibrium is {eq}")
