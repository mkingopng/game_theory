"""

"""
import numpy as np
import nashpy as nash
from random import *

# can we model the 1 - 100 game with 100 players
chosen_number = {}
players = range(1, 100)
number = randint(1, 100)

# print(numbers)

for player in players:
    chosen_number.append({player, number})

print(number)

pyBNEq

# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_11 = nash.Game(player_1, player_2)
# print(game_11)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_11.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q11 are: {eq}")
#
# # answer: true, AA is one of 2 Nash equilibria in this game
