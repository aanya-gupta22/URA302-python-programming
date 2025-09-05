positions = [(2,3), (4,5), (6,7), (7,8)]

even_x_positions = []

for position in positions:
    x = position[0]  
    if x % 2 == 0:
        even_x_positions.append(position)

print("Positions with even x-coordinate:", even_x_positions)
