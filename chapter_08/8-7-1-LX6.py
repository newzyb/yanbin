def make_album(artist, titile):
    artist_album = {
        "artist": artist,
        "title": titile,
    }
    return artist_album


album = make_album("zhangxueyou", "wenbie")
print(album)
