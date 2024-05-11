def make_album(artist, titile, number=None):
    artist_album = {
        "artist": artist,
        "title": titile,
    }
    if number:
        artist_album["number"] = number
    return artist_album


album = make_album("zhangxueyou", "吻别")
print(album)
album = make_album("liudehua", "忘情水")
print(album)
album = make_album("guofucheng", "我对你爱不完", number=8)
print(album)
