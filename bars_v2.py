import nashpy as nash
import numpy as np

row = np.array([[90, 120, 120], [80, 120, 160], [100, 100, 150]])
column = np.array([[90, 80, 100], [120, 120, 100], [120, 160, 150]])
bars_v2 = nash.Game(row, column)
print(bars_v2)
equilibria = bars_v2.support_enumeration()
for eq in equilibria:
    print(f"The unique Nash equilibrium is {eq}")

