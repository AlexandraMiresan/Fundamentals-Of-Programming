from datetime import datetime
from itertools import filterfalse

from src.domain.IdGenerator import IdGenerator
from src.domain.Rental import Rental
from src.services.ServiceException import ServiceException
from src.services.UndoService import FunctionCall, Operation


class RentalService:
    def __init__(self, rental_repo, movie_repo, client_repo, undo_service):
        self._rental_repository = rental_repo
        self._movie_repository = movie_repo
        self._client_repository = client_repo
        self._undo_controller = undo_service

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

    def filter_rentals(self, client, movie):
        result = []
        for rental in self._rental_repository.get_all_rentals():
            if client is not None and rental.client != client:
                continue
            if movie is not None and rental.movie != movie:
                continue
            result.append(rental)
        return result

    def delete_rental(self, rental_id):
        self._rental_repository.delete_rental(rental_id)


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
        rental = Rental(IdGenerator.generate_unique_id(), movie_id, client_id, now_date, date, None)
        self._rental_repository.rent_a_movie(rental)

        functionRedo = FunctionCall(self._rental_repository.rent_a_movie, rental)
        functionUndo = FunctionCall(self._rental_repository.delete_rental, rental.rental_id)

        self._undo_controller.recordUndo(Operation(functionUndo, functionRedo))
        return rental

    def return_movie(self, rental_id):
        self._rental_repository.return_rental(rental_id)

    def get_all_rentals(self):
        return self._rental_repository.get_all_rentals()


    def most_rented_movies(self):
        list_of_dict_movies = []
        for movie in self._movie_repository.get_all_movies():
            dict = {"movie": movie.title,
                    "movie_id": movie.movie_id,
                    "rented_days": 0}
            list_of_dict_movies.append(dict)
        for rentals in self._rental_repository.get_all_rentals():
            if rentals.returned_date is None:
                date_dif = datetime.now() - rentals.rented_date
            else:
                date_dif = rentals.returned_date - rentals.rented_date
            for rental in list_of_dict_movies:
                for movies in rental:
                    if rental.get(movies) == rentals.movie_id:
                        rental.update({"rented_days": date_dif.days})

        sorted_list_of_dict_movies = sorted(list_of_dict_movies, key=lambda x: x["rented_days"], reverse=True)

        return sorted_list_of_dict_movies

    def most_active_clients(self):
        list_of_dict_clients = []
        for client in self._client_repository.get_all_clients():
            dict = {"client": client.name,
                    "client_id": client.client_id,
                    "rented_days": 0}
            list_of_dict_clients.append(dict)
        for rentals in self._rental_repository.get_all_rentals():
            if rentals.returned_date is None:
                date_dif = datetime.now() - rentals.rented_date
            else:
                date_dif = rentals.returned_date - rentals.rented_date
            for rental in list_of_dict_clients:
                for clients in rental:
                    if rental.get(clients) == rentals.client_id:
                        rental.update({"rented_days": date_dif.days})

        sorted_list_of_dict_clients = sorted(list_of_dict_clients, key=lambda x: x["rented_days"], reverse=True)

        return sorted_list_of_dict_clients


    def late_rentals(self):
        list_of_dict_late_rentals = []
        list_of_movie_id = []
        for rentals in self._rental_repository.get_all_rentals():
            if rentals.due_date < rentals.returned_date or (rentals.due_date < datetime.now().date() and rentals.returned_date is None):
                dict = {"movie": "",
                        "movie_id": rentals.movie_id,
                        "rented_days": 0}

                if dict["movie_id"] not in list_of_movie_id:
                    list_of_dict_late_rentals.append(dict)
                list_of_movie_id.append(dict["movie_id"])
                if rentals.returned_date is None:
                    date_dif = datetime.now() - rentals.due_date
                else:
                    date_dif = rentals.returned_date - rentals.due_date
                for rental in list_of_dict_late_rentals:
                    for movies in rental:
                        if rental.get(movies) == rentals.movie_id:
                            rental.update({"rented_days": date_dif.days})

        for movies in self._movie_repository.get_all_movies():
            for rentals in list_of_dict_late_rentals:
                for movie in rentals:
                    if rentals.get(movie) == movies.movie_id:
                        rentals.update({"movie": movies.title})

        sorted_list_of_dict_late_rentals = sorted(list_of_dict_late_rentals, key = lambda x: x["rented_days"], reverse=True)

        return sorted_list_of_dict_late_rentals





