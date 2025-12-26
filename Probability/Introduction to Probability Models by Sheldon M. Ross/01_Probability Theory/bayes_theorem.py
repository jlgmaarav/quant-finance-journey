# Imagine you have developed an algorithm to detect inefficiencies in the stock market.
# Prior Probability: You know that only 1% of the assets in the market have a real inefficiency (Alpha). P(A) = 0.01.
# Sensitivity (True Positive): If the asset has an inefficiency, your algorithm correctly detects it 99% of the times. P(D|A) = 0.99.
# False Alarm (False Positive): If the asset has NO inefficiency, your algorithm mistakenly signals that it does 5% of the times. P(D|A^c) = 0.05.
# Your Challenge: The algorithm has just triggered a 'Buy' signal for a specific asset. 
# What is the real probability that this asset actually has an inefficiency?"

prior_probability = 0.01 #P(A)
sensitivity = 0.99 #P(D|A)
false_alarm = 0.05 #P(D|A^c)

# P(D) = P(D|A)P(A) + P(D|A^c)P(A^c)
probability_of_D = sensitivity * prior_probability + false_alarm * (1 - prior_probability)

# Bayes Theorem: P(A|D) = P(A)*P(D|A)/P(D)
result = prior_probability * sensitivity / probability_of_D

print(result)
