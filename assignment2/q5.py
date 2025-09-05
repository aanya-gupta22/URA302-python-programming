D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print("Initial dictionary:", D)

D[8] = 8.8
print("(i) After adding key 8:", D)

if 2 in D:
    del D[2]
print("(ii) After removing key 2:", D)

if 6 in D:
    print("(iii) Key 6 is present in the dictionary.")
else:
    print("(iii) Key 6 is NOT present in the dictionary.")

print("(iv) Number of elements:", len(D))

total_value = 0
for value in D.values():
    total_value += value
print("(v) Sum of all values:", total_value)

if 3 in D:
    D[3] = 7.1
print("(vi) After updating key 3:", D)

D.clear()
print("(vii) After clearing the dictionary:", D)
