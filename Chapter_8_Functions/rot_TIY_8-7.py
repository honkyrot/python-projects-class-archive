def make_album(artist_name, album_title, num_of_songs=None):
    if num_of_songs:
        return {"artist name": artist_name, "album title": album_title, "number of songs": num_of_songs}
    else:
        return {"artist name": artist_name, "album title": album_title}


print(make_album(artist_name="Hong", album_title="Rot"))
print(make_album(artist_name="Hong2", album_title="Rot2"))
print(make_album(artist_name="Hong3", album_title="Rot3", num_of_songs=5))
