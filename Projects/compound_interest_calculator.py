# Objective: To master basic programming, flow control, and simple data structures.

# What you must build:

# A Python program that calculates the future value of an investment with compound interest.
# It should prompt the user for: initial capital, annual interest rate, investment period, and compounding frequency (annual, monthly, daily).
# It should display a table year by year with: year, initial capital, interest earned, and final capital.
# It should save the results to a CSV file.
# It should allow for comparing different scenarios (e.g., 5% annual interest vs. 6% annual interest over 20 years).

import csv
from decimal import Decimal, InvalidOperation
import matplotlib.pyplot as plt

def calculate_compound_interest(principal, annual_rate, years, frequency):
    """
    Calculates year-by-year investment growth.
    """
    results = []
    current_balance = Decimal(principal)
    period_rate = annual_rate / Decimal(frequency)
    one = Decimal('1')

    for year in range(1, years + 1):
        year_start_balance = current_balance
        
        current_balance = year_start_balance * (one + period_rate) ** frequency
        interest_this_year = current_balance - year_start_balance
        
        results.append({
            "year": year,
            "start": year_start_balance,
            "interest": interest_this_year,
            "end": current_balance
        })
    return results

def save_to_csv(data, filename):
    """
    Saves results to a CSV file as required.

    """
    with open(filename, "w", newline="", encoding="utf-8") as file: 
        writer = csv.DictWriter(file, fieldnames=["year", "start", "interest", "end"])
        writer.writeheader()
        formatted_data = []
        for row in data:
            formatted_data.append({
                "year": row["year"],
                "start": f"{row['start']:.2f}",
                "interest": f"{row['interest']:.2f}",
                "end": f"{row['end']:.2f}"
            })
            
        writer.writerows(formatted_data)

# Make sure that the input is in the correct format
def get_valid_number(promt):
    while True:
        user_input = input(promt)
        user_input = user_input.replace(",", ".")
        try:
            value = Decimal(user_input)

            if value < 0:
                print("Error: the value must be positive.")
                continue
            return value
        except InvalidOperation:
            print("Error: Input not valid. Please, introduce a number")

def main():
    print("--- Project 1.1: Compound Interest Tool ---")
    pv = get_valid_number("Enter initial capital: ")
    r1 = get_valid_number("Enter annual interest rate for Scenario 1 (e.g., 0.05): ")
    t = int(get_valid_number("Enter investment period (years): "))
    n = int(get_valid_number("Enter compounding frequency (1: annual, 12: monthly, 365: daily): "))

    scenario_1 = calculate_compound_interest(pv, r1, t, n)
    
    print(f"\n--- SCENARIO 1 TABLE ({r1*100}%) ---")
    print(f"{'Year':<5} | {'Initial':<12} | {'Interest':<12} | {'Final':<12}")
    for row in scenario_1:
        print(f"{row['year']:<5} | {row['start']:>12.2f} | {row['interest']:>12.2f} | {row['end']:>12.2f}")

    r2 = get_valid_number("\nEnter interest rate for Scenario 2 to compare: ")
    scenario_2 = calculate_compound_interest(pv, r2, t, n)
    
    final_1 = scenario_1[-1]['end']
    final_2 = scenario_2[-1]['end']
    
    print("\n--- COMPARISON SUMMARY ---")
    print(f"Scenario 1 ({r1*100}%): Final Balance = {final_1:.2f}")
    print(f"Scenario 2 ({r2*100}%): Final Balance = {final_2:.2f}")
    print(f"Difference after {t} years: {abs(final_1 - final_2):.2f}") 

    save_to_csv(scenario_1, "investment_report.csv")
    print("\nMain scenario saved to 'investment_report.csv'.")

    # Gráfica de comparación
    years_list = [row['year'] for row in scenario_1]
    balance_1 = [float(row['end']) for row in scenario_1]
    balance_2 = [float(row['end']) for row in scenario_2]

    plt.figure(figsize=(10, 6))
    plt.plot(years_list, balance_1, label=f"Scenario 1 ({r1*100}%)", marker='o')
    plt.plot(years_list, balance_2, label=f"Scenario 2 ({r2*100}%)", marker='s')
    
    plt.title("Investment Growth Comparison")
    plt.xlabel("Years")
    plt.ylabel("Balance")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()