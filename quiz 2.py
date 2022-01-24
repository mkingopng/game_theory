"""

"""
import numpy as np
import nashpy as nash


# # question 1:
# player_1 = np.array([[1, 2, 0], [3, 1, 5]])  # the row player
# player_2 = np.array([[1, -2, 6], [1, 4, 0]])  # the column player
# game_1 = nash.Game(player_1, player_2)
# print(game_1)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_1.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q1 are: {eq}")

# # question 2:
# player_1 = np.array([[1, 2, 0], [3, 1, 5]])  # the row player
# player_2 = np.array([[1, -2, 6], [1, 4, 0]])  # the column player
# game_2 = nash.Game(player_1, player_2)
# print(game_1)
#
# # find the Nash equilibrium with support enumeration, which returns a generator of all the equilibria
# equilibria = game_2.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q2 are: {eq}")


# question 3:
# player_1 = np.array([[1, 2, 0], [3, 1, 5]])  # the row player
# player_2 = np.array([[1, -2, 6], [1, 4, 0]])  # the column player
# game_3 = nash.Game(player_1, player_2)
# print(game_3)
#
# equilibria = game_3.vertex_enumeration()
# for eq in equilibria:
#     print(eq)
#
# # the is_best_response method returns a pair of booleans that indicate whether the specified strategy is best response
# sigma_r = np.array([0, 1])  # as a strategy for player 1 is not specified we should test for both. It indicates that strategy b is player 1's best response to the strategy for player 2 stated in the q
# sigma_c = np.array([0, 0, 1])  # the questions states a probability 0.5 for strategy c and 0.5 for strategy e
# print(game_3.is_best_response(sigma_r, sigma_c))

# question 4:
player_1 = np.array([[1, 2, 0], [3, 1, 5]])  # the row player
player_2 = np.array([[1, -2, 6], [1, 4, 0]])  # the column player
game_3 = nash.Game(player_1, player_2)
print(game_3)

equilibria = game_3.vertex_enumeration()
for eq in equilibria:
    print(eq)

# question 5:

# question 6:

# question 7:

