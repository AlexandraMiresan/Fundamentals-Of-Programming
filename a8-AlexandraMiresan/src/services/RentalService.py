from datetime import datetime

from src.domain.IdGenerator import IdGenerator
from src.domain.Rental import Rental
from src.services.ServiceException import ServiceException


class RentalService:
    def __init__(self, rental_repo, movie_repo, client_repo):
        self._rental_repository = rental_repo
        self._movie_repository = movie_repo
        self._client_repository = client_repo

    def check_if_client_has_rented(self, client_id):
        for rental in self._rental_repository.get_all_rentals():
            if rental.client_id == client_id:
                if rental.due_date < rental.returned_date:
                    return False

        return True

    def check_if_client_exists(self, client_id):
        for client in self._client_repository.get_all_clients():
            if client.client_id == client_id:
                return True
        return False

    def check_if_movie_exists(self, movie_id):
        for movie in self._movie_repository.get_all_movies():
            if movie.movie_id == movie_id:
                return True
        return False

    def rent_movie(self, movie_id, client_id, date):
        now_date = datetime.today().date()
        if not self._client_repository.get_client_by_id(client_id):
            raise ServiceException("Client does not exist")
        for rental in self._rental_repository.get_all_rentals():
            if rental.due_date < now_date and not rental.returned_date and rental.client_id == client_id:
                raise ServiceException("This client cannot rent another movie")
        if not self._movie_repository.get_movie_by_id(movie_id):
            raise ServiceException("Movie does not exist")
        if date < now_date:
            raise ServiceException("Due date cannot be in the past")
        rental = Rental(IdGenerator.generate_unique_id(), client_id, movie_id, now_date, date, None)
        self._rental_repository.rent_a_movie(rental)

    def return_movie(self, rental_id):
        self._rental_repository.return_rental(rental_id)

    def get_all_rentals(self):
        return self._rental_repository.get_all_rentals()