class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def greed(self):
        print(f"Hello my name is {self.name}, color: {self.color}")


# r1 = Robot("Nad", "Red")
# r1.greed()

# r2 = Robot("Dan", "Blue")
# r2.greed()       


class Airplane:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def fly(self):
        print(f"Hello my model is {self.model}, color: {self.color}")



if __name__ == "__main__":
    demo_robot = Robot("mark", "red")
    print(f"Це демо {demo_robot.name}, кольору {demo_robot.color}")
    demo_robot.greed()

    demo_plane = Airplane("MODEL", "Brown")
    print(f"а це лiтак")
    demo_plane.fly()