# File: finance_calculator.py

# Prompt the user for their financial details
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest (explicit formula)
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display results (format as integers if whole numbers)
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
