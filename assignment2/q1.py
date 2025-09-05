L = [11, 12, 13, 14]
print("Initial list:", L)

L.append(50)
L.append(60)
print("(i) After adding 50 and 60:", L)

L.remove(11)
L.remove(13)
print("(ii) After removing 11 and 13:", L)

L.sort()
print("(iii) Sorted ascending:", L)

L.sort(reverse=True)
print("(iv) Sorted descending:", L)

if 13 in L:
    print("(v) 13 is present in the list.")
else:
    print("(v) 13 is not present in the list.")

print("(vi) Number of elements:", len(L))

print("(vii) Sum of all elements:", sum(L))

odd_sum = sum(x for x in L if x % 2 != 0)
print("(viii) Sum of odd numbers:", odd_sum)

even_sum = sum(x for x in L if x % 2 == 0)
print("(ix) Sum of even numbers:", even_sum)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_sum = sum(x for x in L if is_prime(x))
print("(x) Sum of prime numbers:", prime_sum)

L.clear()
print("(xi) After clearing the list:", L)

del L
print("(xii) List deleted.")
