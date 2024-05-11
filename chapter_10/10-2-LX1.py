from pathlib import Path

path = Path("H:/Visual Studio Code/Python-3-ZYB/chapter_10/learning_python.txt")
continues = path.read_text()

lines = continues.splitlines()
for line in lines:
    line = line.replace("Python", "C")
    print(line)
