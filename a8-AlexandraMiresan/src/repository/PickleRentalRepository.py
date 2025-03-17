import pickle

from src.repository.IOException import IOException
from src.repository.RentalRepository import RentalRepository


class PickleRentalRepository(RentalRepository):
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

    def rent_a_movie(self, rental_id):
        super().rent_a_movie(rental_id)
        self.__save_file()

    def __save_file(self):
        try:
            file = open(self._file_name, "wb")
            pickle.dump(self._rental_list, file)
            file.close()
        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def return_rental(self, rental_id):
        super().return_rental(rental_id)
        self.__save_file()