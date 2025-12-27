# We are going to solve problems 25, 26, 27. All are about combinatorics.

# 25. Two cards are randomly selected from a deck of 52 playing cards.
# (a) What is the probability they constitute a pair (that is, that they are of the same denomination)?
# (b) What is the conditional probability they constitute a pair given that they are of different suits?


# To solve this problem, we can think like this: we take out 1 card, that card has 3 that can constitute a pair on the deck (51 cards now), so the probability is 3/51 or 0,0588.
# To probe this thinking process, we are going to execute a montecarlo simulation randomizing the two cards obtained and the compute the probability. 

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