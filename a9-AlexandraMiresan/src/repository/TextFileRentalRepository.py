from pygments.lexers import find_lexer_class_by_name

from src.domain.Rental import Rental
from src.repository.IOException import IOException
from src.repository.RentalRepository import RentalRepository


class TextFileRentalRepository(RentalRepository):
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
                super().add_client(Rental(tokens[0], tokens[1]))
                line = fin.readline()
            fin.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def rent_a_movie(self, rental_id):
        super().rent_a_movie(rental_id)
        self.__save_file()

    def __save_file(self):
        try:
            fout = open(self._file_name, "wt")
            for rental in self.get_all_rentals():
                fout.write(str(rental.rental_id) + "|" + str(rental.movie_id) + "|"
                         + str(rental.client_id) + "|" + str(rental.rented_date) + "|"
                         + str(rental.due_date) + "|" + str(rental.returned_date) + "\n")
            fout.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def return_rental(self, rental_id):
        super().return_rental(rental_id)
        self.__save_file()
