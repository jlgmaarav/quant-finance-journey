# We are going to solve problems 25, 26, 27. All are about combinatorics.

# 25. Two cards are randomly selected from a deck of 52 playing cards.
# (a) What is the probability they constitute a pair (that is, that they are of the same denomination)?
# (b) What is the conditional probability they constitute a pair given that they are of different suits?


# To solve this problem, we can think like this: we take out 1 card, that card has 3 that can constitute a pair on the deck (51 cards now), so the probability is 3/51 or 0,0588.
# To probe this thinking process, we are going to execute a montecarlo simulation randomizing the two cards obtained and the compute the probability. 
"""
import random

def montecarlo_simulation(n_iterations):
    deck = list(range(1, 14)) * 4 #We create the whole deck
    successes = 0

    for _ in range(0, n_iterations):
        hand = random.sample(deck, 2)

        if hand[0] == hand[1]:
            successes += 1
    
    return successes / n_iterations
    

num = int(input("Write the number of iterations wanted: "))
result = montecarlo_simulation(num)
print(result)

"""

# 26. A deck of 52 playing cards, containing all 4 aces, is randomly divided into 4 piles of 13 cards each. Deﬁne events E1, E2, E3, and E4 as follows:
# E1 = {the ﬁrst pile has exactly 1 ace},
# E2 = {the second pile has exactly 1 ace}, 
# E3 = {the third pile has exactly 1 ace}, 
# E4 = {the fourth pile has exactly 1 ace}

# Use Exercise 23 to ﬁnd P(E1E2E3E4), the probability that each pile has an ace.
"""
import math

# We can think of this as the probability of E1, then, the probability of E2 if E1, then, the probability of E3 if E1E2 and so on and so for. 

# p_EX = favorable cases / total cases

p_E1 = math.comb(4, 1) * math.comb(48, 12) / math.comb(52, 13)

p_E2_if_E1 = math.comb(3, 1) * math.comb(36, 12) / math.comb(39, 13)

p_E3_if_E1E2 = math.comb(2, 1) * math.comb(24, 12) / math.comb(26, 13)

p_E4_if_E1E2E3 = math.comb(1, 1) * math.comb(12, 12) / math.comb(13, 13)

p_E1E2E3E4 = p_E1 * p_E2_if_E1 * p_E3_if_E1E2 * p_E4_if_E1E2E3

print(p_E1E2E3E4)

"""


# Let's verify this with Montecarlo, computing it we obtained: 0.1054981992797119

import random

def montecarlo_simulation(n_iterations):
    success = 0

    for _ in range(0, n_iterations):
        deck = list(range(1, 14)) * 4
        random.shuffle(deck)
        pile1 = [deck.pop() for _ in range(13)]
        pile2 = [deck.pop() for _ in range(13)]
        pile3 = [deck.pop() for _ in range(13)]
        pile4 = [deck.pop() for _ in range(13)]

        if 1 in pile1 and 1 in pile2 and 1 in pile3 and 1 in pile4:
            success += 1
    
    return success / n_iterations

num = int(input("Write the number of iterations: "))
result = montecarlo_simulation(num)
print(result)


    