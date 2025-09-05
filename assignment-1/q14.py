N = int(input("Enter a positive integer: "))

if N <= 1:
    print(f"{N} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{N} is a prime number.")
    else:
        print(f"{N} is not a prime number.")
