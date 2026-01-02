# Objective: To master basic programming, flow control, and simple data structures.

# What you must build:

# A Python program that calculates the future value of an investment with compound interest.
# It should prompt the user for: initial capital, annual interest rate, investment period, and compounding frequency (annual, monthly, daily).
# It should display a table year by year with: year, initial capital, interest earned, and final capital.
# It should save the results to a CSV file.
# It should allow for comparing different scenarios (e.g., 5% annual interest vs. 6% annual interest over 20 years).


initial_capital = float(input("Enter your initial capital: "))
annual_interest = float(input("Enter the annual interest: "))
investment_period = int(input("Enter the investment period (in years): "))
compounding_frequency = int(input("Enter the compounding frequency (annual (enter 1), monthly (enter 12), daily (enter 365)): "))

for i in range(1, investment_period + 1):
    C = (1 + annual_interest / compounding_frequency) ** (compounding_frequency * i)
    future_value = initial_capital * C

    if i == 1:
        table_file = open("table.txt", "w")
        table_file.write(f"Year {i}: {future_value} \n")
    else: 
        table_file = open("table.txt", "a")
        table_file.write(f"Year {i}: {future_value} \n")





