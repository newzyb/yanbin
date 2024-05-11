from pathlib import Path
def count_common_words(filename, word):
    path = Path(f"C:/Users/Administrator.USER-20150416CC/Code/Python-3-ZYB/chapter_10/{filename}")
    try:
        countents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        word_count = countents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)
filename= "alice.txt"
count_common_words(filename, "the")


