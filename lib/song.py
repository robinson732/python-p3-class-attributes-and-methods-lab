class Song:
    count = 0                 # total number of songs
    genres = []               # unique list of genres
    artists = []              # unique list of artists
    genre_count = {}          # counts of songs per genre
    artist_count = {}         # counts of songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # increment total song count
        Song.add_song_to_count()
        # add artist and genre to the class lists
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        # update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # Increment total song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Add a new genre if it's not already in the list
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Add a new artist if it's not already in the list
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Update the count of songs for this genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Update the count of songs for this artist
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

