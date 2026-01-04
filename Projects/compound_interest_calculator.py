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

with open("investment_report.csv", "w", encoding="utf-8") as file:
    file.write("Year, Initial Capital, Interest Gained, Future value\n")

    for i in range(1, investment_period + 1):
        future_value = initial_capital * (1 + annual_interest / compounding_frequency) ** (compounding_frequency * i)

        interest_gained = future_value - initial_capital

        file.write(f"{i},{initial_capital:.2f}, {interest_gained:.2f}, {future_value:.2f}")

        compund_capital = initial_capital





