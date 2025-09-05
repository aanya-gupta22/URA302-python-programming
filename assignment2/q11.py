text = input("Enter the string: ")

substring = "emma"
sub_len = len(substring)
count = 0

for i in range(len(text) - sub_len + 1):
    
    part = ""
    for j in range(sub_len):
        part += text[i + j]
  
    if part == substring:
        count += 1

print(f'The substring "{substring}" appears {count} times.')
