"""
Bet with your friend on a die roll. If it rolls a 1, you get $100. If it rolls anything else, they get $100. They’re sure to take it. 

If you lose, find another friend and do the same thing, but now with double the stakes. 

Keep doing this until you win, which you eventually will. Then, you’re guaranteed to net winnings of $100. 

Not impressed? Replace $100 with $1,000,000. Always trust the grind.
"""
import random

def martingala_simulation(initial_capital, goal_win, bet_base=100):
    balance = initial_capital
    current_bet = bet_base
    
    while balance > 0 and balance < initial_capital + goal_win:
        dice = random.randint(1, 6) 
        
        if dice == 1:
            balance += current_bet
            return balance - initial_capital 
        else:
            balance -= current_bet
            current_bet *= 2

            if current_bet > balance:
                current_bet = balance
    
    return balance - initial_capital, 

capital = int(input("Your initial capital (ex. 10000): "))
result = martingala_simulation(capital, 100)
print(f"Net result: {result}")
