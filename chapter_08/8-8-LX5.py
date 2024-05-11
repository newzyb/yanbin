def make_album(artist, titile, number=None):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if number:
        album_dict["number"] = number
    return album_dict


# 意会错了，不知道input后，就是直接与用户互动了，让用户输入文字内容。
artist = input("you like artist is: ")
titile = input("title is:")
album_dict["artist"] = titile

print("please 'quit' is exit.")
while True:
    if artist == "quit":
        break
    if titile == "quit":
        break


msg = make_album
print(msg)
