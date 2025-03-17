from faker import Faker

from src.domain.Movie import Movie


class MovieGenerator:
    def __init__(self):
        self.__faker = Faker()


    def generate_valid_movie(self):
         id = self.__faker.unique.random_number(digits = 3)
         title = self.__faker.sentence(4, True)
         description = self.__faker.sentence(10, True)
         genre = self.__faker.word(ext_word_list= ["Thriller", "Action", "Romance", "Anime", "Horror", "Fantasy"])
         movie = Movie(id, title, description, genre)
         return movie


