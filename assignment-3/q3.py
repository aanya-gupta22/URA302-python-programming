def reverse_string(s):
    reversed_str = ""

    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

input_str = "robot"
output_str = reverse_string(input_str)
print("Reversed string:", output_str)
