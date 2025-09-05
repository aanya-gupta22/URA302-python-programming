num = int(input("Enter a number: "))

is_even = (num % 2 == 0)

if is_even:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
