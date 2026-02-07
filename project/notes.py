from file_utils import read_notes, add_notes


def show_notes():
    notes = read_notes()
    if not notes:
        print("empty")
    else:
        for note in notes:
            print(f"Note: \n{note}")

def create_note():
    text = str(input("Write text: "))
    if not text:
        print("No text")
    else:
        add_notes(text)
        print("Saved")

create_note()
show_notes()