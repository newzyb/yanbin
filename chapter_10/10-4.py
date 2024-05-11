from pathlib import Path

path = Path("H:/Visual Studio Code/Python-3-ZYB/chapter_10/guest.txt")

name = input("What is you name?")
path.write_text(name)
