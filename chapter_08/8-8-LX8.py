def make_album(artist, titile, number=None):
    album_dict = {
        "artist": artist.title(),
        "titile": titile.title(),
    }
    if number:
        album_dict["number"] = number
    return album_dict


artist_name = "please input artist is name: "
titile_name = "titile name is: "
print("input 'quit' is exit.")
while True:
    artists = input(artist_name)
    if artists == "quit":
        break
    titiles = input(titile_name)
    if titiles == "quit":
        break
    artist_album = make_album(artists, titiles)
    print(artist_album)
