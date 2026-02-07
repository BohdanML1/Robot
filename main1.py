from le import Robot, Airplane

robots = []
airplanes = []

while True:
    print("\nЩо створити? (1 - Робот, 2 - Літак, стоп - завершити)")
    choice = input("Введи вибір: ")

    if choice.lower() == "стоп":
        break

    if choice == "1":
        name = input("Введи ім'я робота: ")
        color = input("Введи колір робота: ")
        new_robot = Robot(name, color)
        robots.append(new_robot)

    elif choice == "2":
        model = input("Введи модель літака: ")
        color = input("Введи колір літака: ")
        new_plane = Airplane(model, color)
        airplanes.append(new_plane)

    else:
        print("Невірний вибір, спробуй ще раз.")

# Всі роботи вітаються
print("\nВітаємо всіх роботів!")
for robot in robots:
    robot.greed()

# Всі літаки злітають
print("\nВсі літаки злітають!")
for plane in airplanes:
    plane.fly()