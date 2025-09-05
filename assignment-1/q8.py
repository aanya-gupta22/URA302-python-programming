num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"\nBefore swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = num2, num1

num1 += 1

print(f"\nAfter swapping and incrementing num1:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")
