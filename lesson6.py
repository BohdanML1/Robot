# *args **kwargs
# def x(*philipp):
#     print(philipp)
# x(1, 2, 3, 4)


# def x(name, *point):
#     print("gamer", name)
#     print("points", point)
#     print("сумма", sum(point))

# x("philipp", 10, 15, 1241245)


# def x(**kwargs):
#     print(kwargs)
# x(name="Philipp", age=12, city="Kiyw")


# def x(**philipp):
#     for key, value in philipp.items():
#         print(key, ":", value)
# x(name="boris", age=30, job="tik tok")


# def x(a, b, *args, **kwargs):
#     print("a, b", a, b)
#     print("args", args)
#     print("kwargs", kwargs)
# x(12, 32, 1,2,3,name="philipp", age="12")


# def x():
#     pass
# x()


#####lambda = анонiмна функцiя

# def x(a, b ):
#     return a + b
# print(x(1, 3.12))


# x = lambda a, b: a + b 
# print(x(1, 32))


# x = lambda: print("hello")
# x()


journal = {}

def add_student(name, grades=None):
    if grades is None:
        grades = []
    journal[name] = grades
    print(f"Учень {name}  доданий")

def add_grades(name, *grades):
    if name not in journal:
        print("Такого учня нема")
        return
    for g in grades:
        if 1 <= g <= 12:
            journal[name].append(g)
        else:
            print(f"Оцiнка {g} пропущена")
    print(f"Оцiнки доданi для {name}")

def show_journal():
    print("\nШкiльний журнал")
    if not journal:
        print("Журнал порожнiй")
        return
    for name, grades in journal.items():
        print(f"{name}: {grades}")

def average_grade(name):
    if name not in journal:
        print("Такого учня нема")
        return
    if not journal[name]:
        print("Нема оцiнок")
        return
    avg = sum(journal[name]) / len(journal[name])
    print(f'Середнiй бал {name}: {avg:.2f}')

def class_info(**info):
    print("\nIнфо про класс")
    for k, v in info.items():
        print(f'{k}: {v}')

def best_student():
    best_name = None
    best_avg = 0

    for name, grades in journal.items():
        if grades:
            avg = sum(grades) / len(grades)
            if avg > best_avg:
                best_avg = avg
                best_name = name

    if best_name:
        print(f"🏆 Найкращий учень: {best_name} ({best_avg:.2f})")
    else:
        print("❌ Нема даних для визначення")

while True:
    print("""
=========================
🏫 ШКІЛЬНИЙ ЖУРНАЛ
=========================
1 — Додати учня
2 — Додати оцінки
3 — Показати журнал
4 — Середній бал учня
5 — Інформація про клас
6 — Найкращий учень
0 — Вихід
""")

    choice = input("👉 Обери дію: ")

    if choice == "1":
        name = input("Імʼя учня: ")
        add_student(name)

    elif choice == "2":
        name = input("Імʼя учня: ")
        grades_input = input("Введи оцінки через пробіл: ")
        grades = map(int, grades_input.split())
        add_grades(name, *grades)

    elif choice == "3":
        show_journal()

    elif choice == "4":
        name = input("Імʼя учня: ")
        average_grade(name)

    elif choice == "5":
        class_info(
            class_name="5-А",
            teacher="Пані Ольга",
            students=len(journal)
        )

    elif choice == "6":
        best_student()

    elif choice == "0":


    else:
        print("❌ Невірний вибір")