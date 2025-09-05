principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))
n = float(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

print(f"Compound Interest is: {compound_interest:.2f}")
print(f"Total Amount after {time} years is: {amount:.2f}")
