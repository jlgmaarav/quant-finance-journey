# Problem:
# Compute the probability of the sum of two dices is 8, if at least 1 is a 5

# We create the sample space
sample_space = [(i, j) for i in range(1,7) for j in range(1,7)]

# We create the list for the tuples
valid_tuples = []
tuples_with_5 = []

for i in sample_space:
    if 5 in i:
        tuples_with_5.append(i)
        if sum(i) == 8:
            valid_tuples.append(i)

# We compute the probability
probability = len(valid_tuples) / len(tuples_with_5)

print(probability)



 