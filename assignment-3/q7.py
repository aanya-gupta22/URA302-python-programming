class RobotActions:
    def robot(self):
        print("Outer function: robot()")

        def move():
            print("Inner function: move()")

        move()  

actions = RobotActions()
actions.robot()
