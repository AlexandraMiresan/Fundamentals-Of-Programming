from src.Validators import ValidatorException
from src.domain.Movie import Movie


class MovieValidator:
    @staticmethod
    def validate(movie):
        if not isinstance(movie, Movie):
            raise TypeError("Movie must be of type 'Movie'")
        if len(str(movie.movie_id)) == 0:
            raise ValidatorException.ValidatorError("Movie id is invalid")
        if len(movie.title) == 0:
            raise ValidatorException.ValidatorError("Movie title is invalid")
        if len(movie.description) == 0:
            raise ValidatorException.ValidatorError("Movie description is invalid")
        if len(movie.genre) == 0:
            raise ValidatorException.ValidatorError("Movie genre is invalid")
