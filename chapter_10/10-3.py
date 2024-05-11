from pathlib import Path

path = Path("H:/Visual Studio Code/Python-3-ZYB/chapter_10/learning_python.txt")
continues = path.read_text()

# 下面这个写法是错误的。
lines = continues.splitlines()
for line in lines.replace("Python", "C"):
    print(line)
