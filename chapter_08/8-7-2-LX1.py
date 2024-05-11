def make_album(artist, album, num_songs=None):

    album_dict = {
        "artist": artist.title(),
        "album": album.title(),
    }

    if num_songs:
        album_dict["num_songs"] = num_songs
    return album_dict


album = make_album("zhangxueyou", "吻别")
print(album)
album = make_album("liudehua", "忘情水")
print(album)
album = make_album("guofucheng", "我对你爱不完", num_songs=8)
print(album)
