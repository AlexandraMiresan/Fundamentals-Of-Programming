from src.domain.Movie import Movie
from src.repository.IOException import IOException
from src.repository.MovieRepository import MovieRepository


class TextFileMovieRepository(MovieRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            fin = open(file_name, "rt")
            line = fin.readline()
            while len(line) > 0:
                tokens = line.split("|")
                super().add_movie(Movie(int(tokens[0]), tokens[1], tokens[2], tokens[3].strip()))
                line = fin.readline()
            fin.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def add_movie(self, movie_to_add):
        super().add_movie(movie_to_add)
        self.__save_file()

    def __save_file(self):
        try:
            fout = open(self._file_name, "wt")
            for movie in self.get_all_movies():
                fout.write(str(movie.movie_id) + "|" + str(movie.title) + "|"
                           + str(movie.description) + "|" + str(movie.genre) + "\n")
            fout.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def delete_movie(self, movie_id):
        super().delete_movie(movie_id)
        self.__save_file()

    def update_movie(self, movie_to_update):
        super().update_movie(movie_to_update)
        self.__save_file()

