from pathlib import Path

path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/guest_book2.txt")

msg = "\nHi, what's your name? "
msg += "\nEnter 'quit' if you're the last guest."

guest_names = []

while True:
    name = input(msg)
    if name == "quit":
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

file_str = ""
for name in guest_names:
    file_str += f"{name}\n"
path.write_text(file_str)
