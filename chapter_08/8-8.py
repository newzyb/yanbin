def make_album(artist, title, num_songs=0):
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if num_songs:
        album_dict["num_songs"] = num_songs
    return album_dict


title_prompt = "\nwhat album are you thinking of?"
artist_prompt = "who's the artist?"


print("enter 'quit' at time to stop.")

while True:
    title = input(title_prompt)
    if title == "quit":
        break
    artist = input(artist_prompt)
    if artist == "quit":
        break
    album = make_album(artist, title)
    print(album)
print("\nThinks for responding!")
