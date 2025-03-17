import pickle

from src.repository.IOException import IOException
from src.repository.MovieRepository import MovieRepository


class PickleMovieRepository(MovieRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            file = open(file_name, "rb")
            self._movie_list = pickle.load(file)
            file.close()

        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def add_movie(self, movie_to_add):
        super().add_movie(movie_to_add)
        self.__save_file()

    def __save_file(self):
        try:
            file = open(self._file_name, "wb")
            pickle.dump(self._movie_list, file)
            file.close()
        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def delete_movie(self, movie_id):
        super().delete_movie(movie_id)
        self.__save_file()

    def update_movie(self, movie_to_update):
        super().update_movie(movie_to_update)
        self.__save_file()

