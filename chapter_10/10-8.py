from pathlib import Path
filenames = ['alice.txt', 'dogs.txt']


for filename in filenames:
    print(f"\nReading file: {filename}")
    path = Path(f"C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/{filename}")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents)

