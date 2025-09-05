class RobotMover:
    def move_robot(self, x, y, direction):
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        else:
            print("Invalid direction!")
        return (x, y)


mover = RobotMover()
new_pos = mover.move_robot(0, 0, "up")
print("New position:", new_pos)
