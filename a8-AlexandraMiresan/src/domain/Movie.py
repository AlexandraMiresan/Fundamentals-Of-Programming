class Movie:
    def __init__(self, movie_id:int, title:str, description:str, genre:str):
        self._movie_id = movie_id
        self._title = title
        self._description = description
        self._genre = genre

    def __str__(self):
        return "Movie ID: " + str(self.movie_id) + " The movie: " + self._title + " is about " + self._description + " and its genre is " + self._genre + "."

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def genre(self):
        return self._genre

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_genre(self, genre):
        self._genre = genre



