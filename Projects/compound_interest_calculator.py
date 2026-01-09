# Objective: To master basic programming, flow control, and simple data structures.

# What you must build:

# A Python program that calculates the future value of an investment with compound interest.
# It should prompt the user for: initial capital, annual interest rate, investment period, and compounding frequency (annual, monthly, daily).
# It should display a table year by year with: year, initial capital, interest earned, and final capital.
# It should save the results to a CSV file.
# It should allow for comparing different scenarios (e.g., 5% annual interest vs. 6% annual interest over 20 years).

import csv

def calculate_compound_interest(principal, annual_rate, years, frequency):
    """
    Calculates year-by-year investment growth.
    """
    results = []
    current_balance = principal
    period_rate = annual_rate / frequency
    
    for year in range(1, years + 1):
        year_start_balance = current_balance

        current_balance = year_start_balance * (1 + period_rate) ** frequency
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
        writer.writerows(data)

def main():
    print("--- Project 1.1: Compound Interest Tool ---")
    
    pv = float(input("Enter initial capital: "))
    r1 = float(input("Enter annual interest rate for Scenario 1 (e.g., 0.05): "))
    t = int(input("Enter investment period (years): "))
    n = int(input("Enter compounding frequency (1: annual, 12: monthly, 365: daily): "))

    scenario_1 = calculate_compound_interest(pv, r1, t, n)
    
    print(f"\n--- SCENARIO 1 TABLE ({r1*100}%) ---")
    print(f"{'Year':<5} | {'Initial':<12} | {'Interest':<12} | {'Final':<12}")
    for row in scenario_1:
        print(f"{row['year']:<5} | {row['start']:>12.2f} | {row['interest']:>12.2f} | {row['end']:>12.2f}")

    r2 = float(input("\nEnter interest rate for Scenario 2 to compare: "))
    scenario_2 = calculate_compound_interest(pv, r2, t, n)
    
    final_1 = scenario_1[-1]['end']
    final_2 = scenario_2[-1]['end']
    
    print("\n--- COMPARISON SUMMARY ---")
    print(f"Scenario 1 ({r1*100}%): Final Balance = {final_1:.2f}")
    print(f"Scenario 2 ({r2*100}%): Final Balance = {final_2:.2f}")
    print(f"Difference after {t * n} total compounding periods: {abs(final_1 - final_2):.2f}") # Logic used!

    save_to_csv(scenario_1, "investment_report.csv")
    print("\nMain scenario saved to 'investment_report.csv'.")

if __name__ == "__main__":
    main()