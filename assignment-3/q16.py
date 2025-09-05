class Robot:
    def __init__(self, name, task):
        self.name = name
        self.task = task
        self.battery_level = 100  # battery level in percentage

    def perform_task(self):
        if self.battery_level >= 10:
            print(f"{self.name} is performing the task: {self.task}")
            self.battery_level -= 10
        else:
            print(f"{self.name} does not have enough battery to perform the task!")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is fully recharged.")

    def status(self):
        print(f"Robot Name: {self.name}")
        print(f"Current Task: {self.task}")
        print(f"Battery Level: {self.battery_level}%")

robot1 = Robot("Robo1", "Cleaning")
robot1.status()
robot1.perform_task()
robot1.status()
robot1.recharge()
robot1.status()
