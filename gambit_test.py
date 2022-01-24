"""
https://gambitproject.readthedocs.io/en/latest/pyapi.html#python-api
"""

import pygambit
import numpy as np

# g = pygambit.Game.new_tree()
# g.title = "A simple poker example"
# p = g.players.add("Alice")

#
g = pygambit.Game.new_table([2, 2])
g.title = "A prisoner's dilemma game"
g.players[0].label = "Alphonse"
g.players[1].label = "Gaston"

# strategies collection for a player
g.players[0].strategies[0].label = "Cooperate"
g.players[0].strategies[1].label = "Defect"

m = np.array([[8, 2], [10, 5]], dtype=pygambit.Rational)
g = pygambit.Game.from_arrays(m, np.transpose(m))

print(g.players[0].strategies)

# iterating the pure strategy profiles in a game
g = pygambit.Game.read_game("e02.nfg")
list(g.contingencies)

for profile in g.contingencies:
    print(profile, g[profile][0], g[profile][1])

# mixed strategy and behaviour profiles. 3 possible methods.
g = pygambit.Game.read_game("e02.nfg")
p = g.mixed_strategy_profile()

# first method
list(p)

# second method
print(p[g.players[0]])

# third method
print(p[g.players[1].strategies[0]])

# the expected payoff to a player using a mixed strategy profile
p.payoff(g.players[0])

# the standalone expected payoff
print(p.strategy_value(g.players[0].strategies[2]))

# A MixedBehaviorProfile object, which represents a probability distribution over the actions at each information set,
# is constructed using Game.mixed_behavior_profile(). Behavior profiles are initialized to uniform randomization over
# all actions at each information set.
g = pygambit.Game.read_game("e02.efg")
p = g.mixed_behavior_profile()
list(p)
print(p[g.players[0]])
print(p[g.players[0].infosets[0]])
print(p[g.players[0].infosets[0].actions[0]])

# computing Nash equilibria
g = pygambit.Game.read_game("e02.nfg")
solver = pygambit.nash.ExternalEnumPureSolver()  # pure equilibria
solver.solve(g)

solver = pygambit.nash.ExternalEnumMixedSolver()  # mixed equilibria
solver.solve(g)

solver = pygambit.nash.ExternalLogitSolver()  #
solver.solve(g)


#
g = pygambit.Game.read_game("e02.efg")
solver = pygambit.nash.ExternalLCPSolver()
solver.solve(g)  # mixed behaviour profile

solver.solve(g, use_strategic=True)  # mixed strategy profile


#
g = pygambit.Game.read_game("e02.efg")
pygambit.nash.lcp_solve(g)
pygambit.nash.lcp_solve(g, rational=True)
pygambit.nash.lcp_solve(g, use_strategic=True)
pygambit.nash.lcp_solve(g, use_strategic=True, rational=True)
