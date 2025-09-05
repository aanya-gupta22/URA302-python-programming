S1 = [10, 20, 30, 40, 50, 60]
S2 = [40, 50, 60, 70, 80, 90]

print("Initial S1:", S1)
print("Initial S2:", S2)

for item in [55, 66]:
    if item not in S1:
        S1.append(item)
print("(i) After adding 55 and 66 to S1:", S1)

for item in [10, 30]:
    if item in S1:
        S1.remove(item)
print("(ii) After removing 10 and 30 from S1:", S1)

if 40 in S1:
    print("(iii) 40 is present in S1.")
else:
    print("(iii) 40 is NOT present in S1.")

union = S1[:]  
for item in S2:
    if item not in union:
        union.append(item)
print("(iv) Union of S1 and S2:", union)

intersection = []
for item in S1:
    if item in S2:
        intersection.append(item)
print("(v) Intersection of S1 and S2:", intersection)

difference = []
for item in S1:
    if item not in S2:
        difference.append(item)
print("(vi) Difference S1 - S2:", difference)
