def make_album(artist_name, album_title,songs=None):
    album = {"artist_name": artist_name, "album_title":album_title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print(f"\nTo quit at anytime, enter 'q'")
    album_artist_name = input("What is the artist's name?")
    if album_artist_name == "q":
        break
    album_title = input("What is the album's title?")
    if album_title == "q":
        break
    album_songs = input("How many songs are there in this album?")
    if album_songs == "q":
        break
    new_album= make_album(album_artist_name,album_title,album_songs)
    print(new_album)