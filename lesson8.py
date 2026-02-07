#read
# try:
#     file = open("lesson.txt", "r")
#     content = file.()
#     print("вмiст файлу: ")
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("файл не знайдено")

#write
# try:
#     file = open("lesson.txt", "w")
#     file.write("Hello world!")
#     file.write("Hi harry poter")
#     file.close()
#     print("file записанно")
# except:
#     print("помилка")

#add 
# file = open("lesson.txt", "a")
# file.write("\nbbbb")
# file.close()


# file = open("lesson.txt", "r")
# for line in file: 
#     print("рядок з тексту", line.strip())
# file.close()



# with open("lesson.txt", "r") as file:
#     content = file.read()
#     print(content)


file = open("lesson.txt", "r+")
content = file.read()
print("старий текст", content)
file.write("New text")
file.close


# file = open("onless.txt", "w")
# file.write("New file")
# file.seek()
# print(file.read())
# file.close()



