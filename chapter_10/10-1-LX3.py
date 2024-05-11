from pathlib import Path
path = Path("C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/learning_python.txt")
contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)
    
