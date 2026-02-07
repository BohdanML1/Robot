# student = {
#     "Name": "Ihor",
#     "Age": 12,
#     "Grate": 6
# }
# student["Age"] = student["Age"] + 1
# student["School"] = "Rak"
# # for key, value in student.items():
# #     print(key, "-", value)
# if "Age" in student:
#     print("Ключ э")
# else:
#     print("ключа нема")    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# questions = {
#     "Скільки лап у кота?": "4",
#     "Якого кольору небо?": "синє",
#     "2 + 2 = ?": "4",
#     "Столиця України?": "київ",
#     "Скільки днів у тижні?": "7"
# }

# score = 0
# print("🎮 Ласкаво просимо у гру!")
# print("Відповідай на питання. Пиши відповідь і тисни Enter.")
# print("--------------------------------------------------")

# while True: 
#     for question, answer in questions.items():
#         user_Answer = input(question + " ").lower()

#         if user_Answer == answer:
#             print("right")
#             score += 1
#         else:
#             print("false", answer)
#         print("Твій рахунок:", score)
#         print("-------------------------")
    
#     play_again = input("one more time? (yes/no): ").lower()
#     if play_again != "no":
#         print("thank you")
#         print("your score", score)
#         break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# easy = {
#     "2 + 2 = ?": "4",
#     "Скільки лап у собаки?": "4",
#     "Колір сонця?": "жовтий"
# }

# medium = {
#     "5 + 7 = ?": "12",
#     "Столиця України?": "київ",
#     "Скільки місяців у році?": "12"
# }

# hard = {
#     "9 * 8 = ?": "72",
#     "Найбільша планета?": "юпітер",
#     "Скільки хвилин у годині?": "60"
# }

# print("🎮 ВІКТОРИНА")
# print("1 — Легко")
# print("2 — Середньо")
# print("3 — Складно")

# level = input("обери левел (1/2/3): ")
# if level == "1":
#     questions = easy
# elif level == "2":
#     questions = medium
# else:
#     questions = hard

# score = 0
# lives = 3
# used_hint = False

# print("Гра почалась! У тебе 3 життя ❤️")

# for question, answer in questions.items():
#     print("\n❓", question)
#     print("Напиши відповідь або 'підказка'")

#     user_answer = input("👉 ").lower()

#     if user_answer == "підказка" and not used_hint:
#         print("💡 Підказка: відповідь починається з літери:", answer[0])
#         used_hint = True
#         user_answer = input("👉 ").lower()
#     if user_answer == answer:
#         print("✅ Правильно!")
#         score += 1
#     else:
#         lives -= 1
#         print("❌ Неправильно. Правильно:", answer)
#         print("❤️ Життів залишилось:", lives)
    
#     if lives == 0:
#         print("\n game over")
#         break
# print("\n🏁 КІНЕЦЬ ГРИ")
# print("🏆 Рахунок:", score)



# def hello():
#     print("hello")


# def grid(name):
#     print(f"Привiт {name}")


# grid("Iван")


# def green(a, b):
#     return a + b

# x = green(2, 2)
# print(x)

# def test():
#     print("start")
#     return
#     print("stop")

# test()


# def x(age):
#     if age >= 18:
#         return "дорослий"
#     return "дитина"

# a = int(input("введи: "))
# result = x(a)
# print(f"тобi {result}")
# return 10
# return "hello"
# return True
# return [1,2,3]


# def x():
#     for i in range(1, 6):
#         print(i)
# x()


# def x():
#     password = ""

#     while password != "1234":
#         password = input("введи пароль ")
#     print("доступ дозволено")
# x()


# def login():
#     return input("login: ")

# def password():
#     return input("password: ")

# def auth():
#     if login() == "admin" and password() == "1234":
#         print("доступ дозволено")
#     else:
#         print("пмилка")
# auth()


# def grid(name="announ"):
#     print(f"привiт{name}")
# grid("Hpilipp")

# def x():
#     return "Philipp", 30
# name, age = x()
# print(name, age)


balance = 0
def add_money(ammount):
    global balance
    balance += ammount
    print(f"додано {ammount}, balance { balance} грн.")

def remove_money(ammount):
    global balance
    if ammount > balance:
        print("недостатньо грошей")
    else:
        balance -= ammount
        print(f"знято {ammount} грн. balance {balance} грн.")

def show_balance():
    print(f"ваш баланс {balance} грн.")

while True:
    print(" \n вибери дiю: ")
    print("1 - додати грошi")
    print("2 - зняти грошi")
    print("3 - показати баланс")
    print("4 - вийти ")

    choise = input("твiй вибiр")
    if choise == "1":
        ammount = int(input("введи сумму"))
        add_money(ammount)
    elif choise == "2":
        ammount = int(input("введи сумму для зняття"))
        remove_money(ammount)
    elif choise == "3":
        show_balance()
    elif choise == "4":
        print("допобаченя")
        break
    else:
        print("невiрний вибiр")


