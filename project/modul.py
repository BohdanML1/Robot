def read_notes(): 

    try:
        with open("notes.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return[]
    


def add_notes(text):

    try:
        with open("notes.txt", "a") as file:
            return file.write(text + "\n")
    except:
        print("помилка")


