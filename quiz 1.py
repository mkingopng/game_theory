"""
quiz 1 checking
"""
import numpy as np
import nashpy as nash

# definition: A pure-strategy Nash equilibrium is an action profile with the property that no single player i can
# obtain a higher payoff by choosing an action different from ai, given every other player j adheres to aj.


# question 1: AA is a pure strategy Nash equilibrium of this game, true or false?
player_1 = np.array([[2, -2], [2, -2]])  # the row player
player_2 = np.array([[2, 2], [-2, -2]])  # the column player
game_1 = nash.Game(player_1, player_2)
print(game_1)

# find the Nash equilibrium with support enumeration
equilibria = game_1.support_enumeration()
for eq in equilibria:
    print(f"the equilibria for q1 are: {eq}")
# # mk: 4x equilibria are found, so the answer is: True


# question 2: AB is a pure strategy Nash equilibrium of this game, true or false?
# player_1 = np.array([[2, -2], [2, -2]])  # the row player
# player_2 = np.array([[2, 2], [-2, -2]])  # the column player
# game_2 = nash.Game(player_1, player_2)
# print(game_2)

# find the Nash equilibrium with support enumeration
# equilibria = game_2.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q2 are: {eq}")
# mk: 4x equilibria are found, so the answer is: True


# question 3: BA is a pure strategy Nash Equilibrium of this game, true or false?
# player_1 = np.array([[2, -2], [2, -2]])  # the row player
# player_2 = np.array([[2, 2], [-2, -2]])  # the column player
# game_3 = nash.Game(player_1, player_2)
# print(game_3)

# find the Nash equilibrium with support enumeration
# equilibria = game_3.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q3 are: {eq}")
# mk: 4x equilibria are found, so the answer is: True


# question 4: BB is a pure strategy Nash equilibrium of this game, true or false?
# player_1 = np.array([[2, -2], [2, -2]])  # the row player
# player_2 = np.array([[2, 2], [-2, -2]])  # the column player
# game_4 = nash.Game(player_1, player_2)
# print(game_4)

# find the Nash equilibrium with support enumeration
# equilibria = game_4.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q4 are: {eq}")
# mk: 4x equilibria are found, so the answer is: True


# question 5: this game is dominance solvable, true or false?
# player_1 = np.array([[2, -2], [2, -2]])  # the row player
# player_2 = np.array([[2, 2], [-2, -2]])  # the column player
# game_5 = nash.Game(player_1, player_2)
# print(game_5)

# find the Nash equilibrium with support enumeration
# equilibria = game_5.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q5 are: {eq}")
# mk: The answer is: True. Both players would never play B as it is dominated. Therefore this game is dominance
#  solvable


# Question 6: This game has at least one inadmissible Nash equilibrium
# check definition of inadmissible Nash equilibrium

# player_1 = np.array([[2, -2], [2, -2]])  # the row player
# player_2 = np.array([[2, 2], [-2, -2]])  # the column player
# game_6 = nash.Game(player_1, player_2)
# print(game_6)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_6.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q6 are: {eq}")
# mk:answer: True. an inadmissible strategy is one that a player would never play because it is always inferior.
#  There is at least one of those in this game


# question 7: in the unique nash equilibrium of this game, player 1 plays...
# player_1 = np.array([[1, 1, 4, 2], [1, 1, 3, 4], [0, 0, 2, 2], [2, 3, 6, 0]])  # the row player
# player_2 = np.array([[0, 2, 1, 1], [2, 4, 0, 2], [3, 1, 0, 0], [4, 2, 1, 1]])  # the column player
# game_7 = nash.Game(player_1, player_2)
# print(game_7)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_7.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q7 are: {eq}")
# mk: answer: player 1 plays strategy D


# question 8: in the unique nash equilibrium of this game, player 2 plays...
# player_1 = np.array([[1, 1, 4, 2], [1, 1, 3, 4], [0, 0, 2, 2], [2, 3, 6, 0]])  # the row player
# player_2 = np.array([[0, 2, 1, 1], [2, 4, 0, 2], [3, 1, 0, 0], [4, 2, 1, 1]])  # the column player
# game_8 = nash.Game(player_1, player_2)
# print(game_8)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_8.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q8 are: {eq}")
# mk: answer: player 2 plays strategy A


# question 9: this game is dominance solvable, true or false?
# player_1 = np.array([[1, 1, 4, 2], [1, 1, 3, 4], [0, 0, 2, 2], [2, 3, 6, 0]])  # the row player
# player_2 = np.array([[0, 2, 1, 1], [2, 4, 0, 2], [3, 1, 0, 0], [4, 2, 1, 1]])  # the column player
# game_9 = nash.Game(player_1, player_2)
# print(game_9)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_9.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q9 are: {eq}")
# mk: answer: True


# question 10: This game has at least one inadmissible Nash equilibrium, true or false?
# player_1 = np.array([[1, 1, 4, 2], [1, 1, 3, 4], [0, 0, 2, 2], [2, 3, 6, 0]])  # the row player
# player_2 = np.array([[0, 2, 1, 1], [2, 4, 0, 2], [3, 1, 0, 0], [4, 2, 1, 1]])  # the column player
# game_10 = nash.Game(player_1, player_2)
# print(game_10)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_10.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q10 are: {eq}")
# mk: answer: False. The unique Nash equilibrium is admissible

# # question 11: AA is a pure strategy Nash equilibrium of this game, True or false?
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_11 = nash.Game(player_1, player_2)
# print(game_11)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_11.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q11 are: {eq}")
# mk: answer: true, AA is one of 2 Nash equilibria in this game


# # question 12: BB is a pure Nash equilibrium of this game.
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_12 = nash.Game(player_1, player_2)
# print(game_12)
#
# # find the Nash equilibrium with support enumeration
# equilibria = game_12.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q12 are: {eq}")
# # answer: true, BB is one of 2 Nash equilibria in this game


# question 13: AB is a pure strategy nash equilibrium of this game
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_13 = nash.Game(player_1, player_2)
# print(game_13)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_13.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q13 are: {eq}")
# # answer: false, AB is NOT one of 2 Nash equilibria in this game


# # question 14: BA is a pure strategy Nash Equilibrium of this game
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_14 = nash.Game(player_1, player_2)
# print(game_14)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_14.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q14 are: {eq}")
# # answer: False, BA is NOT one of 2 Nash equilibria in this game


# # question 15: this game is dominance solvable, True or false?
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_15 = nash.Game(player_1, player_2)
# print(game_15)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_15.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q15 are: {eq}")
# # answer: True, this game is dominance solvable. strategy B is dominant for player 2, player 2 would never play A as
# # it is always inferior
# wk: it is not dominance solvable

# question 16: this game has at least one inadmissible Nash equilibrium
# player_1 = np.array([[3, 4], [2, 4]])  # the row player
# player_2 = np.array([[10, 7], [0, 2]])  # the column player
# game_16 = nash.Game(player_1, player_2)
# print(game_16)
#
# # find the Nash equilibrium with support enumeration
# equilibria= game_16.support_enumeration()
# for eq in equilibria:
#     print(f"the equilibria for q15 are: {eq}")
# mk: answer: True, AA is inadmissible because player_2 would never play strategy A. Strategy B is dominant for player_2
# wk: correct b is inadmissable because b is weakly dominated by A


# question 17: two firms, firm_1 and firm_2 compete by simultaneously choosing prices. Both firms sell an identical
#  product for which each of the 100 consumers has a maximum willingness to pay of $40. Each consumer will buy at most
#  1 unit, and will buy it from whichever firm charges the lowest price. If firms set the same price, they share the
#  market equally. Costs are given by ci(qi) = 16qi. Because of government regulation, firms can only choose prices
#  which are integer numbers, and they cannot price above $40. Answer the following:

# NB: this is a Bertrand game

# question 17a) If firm_1 chooses p1 = 26, firm_2's best response is to sell at what price?

# answer: 25, because firm_2 has incentive to undercut and take the market. the smallest unit allowed is 1.

# question 17b) if firm_2 chooses the price determined in the previous question, firm_1's best response is to choose
#  what price?=40-16


# answer: 24, because firm_1 has incentive to undercut and take the market

# question 17c) if firm_1 chooses p1 = 10, firm_2's best response is to choose what price?
# mk: answer: 16, because 16 is the marginal cost and firm_2 is unwilling to make a loss. Firm_1 is pricing
#  irrationally.

# question 17d) Now suppose both firms are capacity-constrained: firm_1 can produce at most 13 units, and firm_2 can
#  produce at most 40 units. If firms set different prices, consumers will first buy from the firm charging the lower
#  price. Once that firm's supply is exhausted, consumers will buy from the firm charging the higher price. what is
#  firm 1's equilibrium profit?
# mk: answer: 40. because the supply is capacity constrained,and demand = 100 > supply = 53, therefore both firms will
#  sell all stock no matter what price they set, so they will set a price that maximises profit. The highest allowable
#  price is $40?
# wk: false. you have confused price per unit with total profit. the correct answer is 20(40-16) = 480


# question 18: suppose ice cream vendors are distributed along a straight beach of 1km. Each consumer buys 1 icecrea
#  from the closest ice cream cart. If the carts are equidistant from a consumer, he will buy from each of them with
#  equal probability. You have learned what the Nash equilibrium is if 2 carts simultaneously choose where to position
#  themselves. Now suppose there are 3 ice cream carts simultaneously deciding where to position themselves. It is a
#  Nash equilibrium for all three carts to position themselves where the median customer is located
# mk: answer: False. If there are 3 vendors, there is no equilibrium. If all 3 vendors are in the centre, one of them
#  can move slightly to the right or left adn capture nearly half the market which is more than the 1/3 he had before.
# wk: correct


# question 19: There is a pure strategy Nash equilibrium in this game in which one cart sells to no-one
# mk: answer: False. At any point on the beach a cart may be positioned, there are some customers who will be closest to
#  that cart. Furthermore, as above, there is no equilibrium with 3 players.
# wk: correct


# question 20: There is a pure strategy nash equilibrium in this game in which all three carts share the market equally
# mk: False, there is no equilibrium in this game.
# wk: correct
