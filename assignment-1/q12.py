angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
    print("Yes, the angles can form a triangle.")
else:
    print("No, the angles cannot form a triangle.")
