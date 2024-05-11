from pathlib import Path
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(f"C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/{filename}")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
