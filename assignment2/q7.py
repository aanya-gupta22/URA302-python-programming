import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

print("(i) 100 Random Strings:")

for _ in range(100):
    length = random.randint(6, 8) 
    random_string = ""
    for _ in range(length):
        random_string += letters[random.randint(0, len(letters)-1)]
    print(random_string)

print("\n(ii) Prime numbers between 600 and 800:")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for number in range(600, 801):
    if is_prime(number):
        print(number)

print("\n(iii) Numbers between 100 and 1000 divisible by 7 and 9:")

for number in range(100, 1001):
    if number % 7 == 0 and number % 9 == 0:
        print(number)
