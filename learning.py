def make_album(artist_name, album_title,songs=None):
    album = {"artist_name": artist_name, "album_title":album_title}
    if songs:
        album["songs"] = songs
    return album

first_album = make_album("John","John's Album Title")
print(first_album)

second_album = make_album("Dave","Dave's Album Title",90)
print(second_album)