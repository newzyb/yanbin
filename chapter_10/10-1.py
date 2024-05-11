from pathlib import Path

path = Path("H:/Visual Studio Code/Python-3-ZYB/chapter_10/learning_python.txt")
contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
