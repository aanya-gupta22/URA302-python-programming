x, y, z = 3, 4, 6

array_3d = []

for i in range(x):
    layer = []
    for j in range(y):
        row = []
        for k in range(z):
            row.append('*')
        layer.append(row)
    array_3d.append(layer)

for i in range(x):
    print(f"Layer {i+1}:")
    for row in array_3d[i]:
        print(row)
    print()  

