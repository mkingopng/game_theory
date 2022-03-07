"""

"""
import random


x = int(input("What's your input in $: "))
y = random.randint(5, 20)

x_payoff = []
y_payoff = []

if x > y:
    x_payoff = y
    y_payoff = y + 5

elif x < y:
    x_payoff = x + 5
    y_payoff = x

else:
    x_payoff = x
    y_payoff = y

print(f"You entered a compensation of {x} while the computer said {y} .\n"
      f"So, your payoff is {x_payoff} and computer's payoff is {y_payoff}")
