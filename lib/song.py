class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        if genre not in Song.genres:
            Song.genres.append(genre)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

        if artist not in Song.artists:
            Song.artists.append(artist)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

        Song.count += 1

Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artist_count)
