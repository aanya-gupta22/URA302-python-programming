list1 = [10, 15, 20, 25, 30, 35]
list2 = [40, 45, 50, 55, 60, 65]

new_list = []

for num in list1:
    if num % 2 != 0:
        new_list.append(num)

for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print("New list:", new_list)
