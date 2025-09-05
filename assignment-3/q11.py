class RobotPath:
    def is_goal_reached(self, path):
        x, y = 0, 0  

        for move in path:
            if move == "up":
                y += 1
            elif move == "down":
                y -= 1
            elif move == "left":
                x -= 1
            elif move == "right":
                x += 1
            else:
                print(f"Invalid move: {move}")

        if (x, y) == (2, 0):
            return True
        else:
            return False

robot = RobotPath()
path1 = ["up", "right", "right", "down"]
print(robot.is_goal_reached(path1))  

path2 = ["up", "left", "down"]
print(robot.is_goal_reached(path2)) 
