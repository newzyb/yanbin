def make_album(artist, album):
    album_dict = {
        "artist": artist.title(),
        "album": album.title(),
    }
    return album_dict


album = make_album("zhangxueyou", "wenbie")
print(album)
album = make_album("liudehua", "wangwingshui")
print(album)
album = make_album("guofucheng", "woduiniaibuwan")
print(album)
