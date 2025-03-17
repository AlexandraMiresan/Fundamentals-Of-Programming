from src.Validators.MovieValidator import MovieValidator
from src.repository.RepoException import RepoException


class MovieRepository:
    def __init__(self):
        self._movie_list = []

    def get_all_movies(self):
        """returns a list of all movies"""
        return self._movie_list

    def add_movie(self, movie_to_add):
        """adds movies to the repository"""
        for movie in self._movie_list:
            if movie.movie_id == movie_to_add.movie_id:
                raise RepoException("Movie id already exists")

        self._movie_list.append(movie_to_add)

    def get_movie_by_id(self, movie_id):
        for movie in self._movie_list:
            if movie.movie_id == movie_id:
                return movie

    def delete_movie(self, movie_id):
        """deletes a movie from the repository"""
        for movie in self._movie_list:
            if movie.movie_id == movie_id:
                self._movie_list.remove(movie)
                return movie

    def update_movie(self, movie_to_update):
        """updates a movie from the repository"""
        for movie in self._movie_list:
            if movie.movie_id == movie_to_update.movie_id:
                movie.set_title(movie_to_update.title)
                movie.set_description(movie_to_update.description)
                movie.set_genre(movie_to_update.genre)



