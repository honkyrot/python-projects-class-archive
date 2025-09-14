def make_album(artist_name, album_title, num_of_songs=None):
    if num_of_songs:
        return {"artist name": artist_name, "album title": album_title, "number of songs": num_of_songs}
    else:
        return {"artist name": artist_name, "album title": album_title}


created_albums = []

while True:
    in_name = input("What is the artist name?\n> ")
    al_name = input("What is the album name?\n> ")
    try:
        num_song = int(input("How many songs are in the album?\n> "))
    except ValueError:
        print("Not a number!")
        continue
    new_album = make_album(in_name, al_name, num_song)
    created_albums.append(new_album)
    print(new_album)
    cont = input("Continue adding more albums? (y/n)\n> ").lower()
    if cont == "n" or cont == "n":
        break
