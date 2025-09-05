input_str = input("Enter numbers with commas: ")

num_list = input_str.split(',')

num_list = [num.strip() for num in num_list]

num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)
