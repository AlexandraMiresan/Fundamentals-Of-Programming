from datetime import datetime
from random import randint

from faker import Faker

from src.domain.Rental import Rental


class RentalGenerator:
    def __init__(self):
        self.__faker = Faker()

    def generate_valid_rental(self, movies_list, clients_list) -> Rental:
        rental_id = self.__faker.unique.random_number(digits = 4)
        movie_id = movies_list[randint(0, len(movies_list) - 1)].movie_id
        client_id = clients_list[randint(0, len(clients_list) - 1)].client_id
        due_date = datetime.strptime(self.__faker.date('%m-%d-%Y'), '%m-%d-%Y').date()
        rented_date = datetime.strptime(self.__faker.date(end_datetime=due_date, pattern='%m-%d-%Y'), '%m-%d-%Y').date()
        returned_date = self.__faker.date_between(start_date=rented_date)
        return Rental(rental_id, movie_id, client_id, rented_date, due_date, returned_date)

