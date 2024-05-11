def make_album(artist, titile, number=None):
    album_dict = {
        "artist": artist.title(),
        "titile": titile.title(),
    }
    if number:
        album_dict["number"] = number
    return album_dict


# album_dict['number'] = number  这串代码的意思是如果number有数值，就把数值写入字典，并且显示出来。

artist_list = "you like artist is: "
titile_list = "title is:"
# album_dict["artist"] = titile 这个代码是多余的，与课本7.3.3内容混淆了。
# 课本7.3.3写出来这个代码，目的是把输入的内容存储在字典中。
print("please 'quit' is exit.")
while True:
    artists = input(artist_list)
    if artists == "quit":
        break

    titiles = input(titile_list)
    if titiles == "quit":
        break
    album = make_album(artists, titiles)
    print(album)
    # 最后需要打印的代码是在while循环体内的。
