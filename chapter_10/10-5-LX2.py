from pathlib import Path

path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/guest_book1.txt")
msg = "\nHi, what's your name? "
msg += "\nEnter 'quit' if you're the last guest."

guest_name = []
while True:
    name = input(msg)
    if name == "quit":
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_name.append(name)

file_string = ""
for name in guest_name:
    file_string += f"{name}\n"
path.write_text(file_string)
