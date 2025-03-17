from src.Validators import ValidatorException
from src.domain.Rental import Rental


class RentalValidator:
    @staticmethod
    def validate(rental, movies_list, clients_list):
        if not isinstance(rental, Rental):
            raise TypeError("Rental must be of type 'Rental'")
        if len(str(rental.rental_id)) == 0:
            raise ValidatorException.ValidatorError("Rental id is empty")
        if rental.movie_id not in movies_list:
            raise ValidatorException.ValidatorError("The movie does not exist")
        if rental.client_id not in clients_list:
            raise ValidatorException.ValidatorError("The client does not exist")
        if rental.due_date < rental.rented_date:
            raise ValidatorException.ValidatorError("The due date must be greater than the rented date")
        if rental.returned_date < rental.rented_date:
            raise ValidatorException.ValidatorError("The return date must be greater than the rented date")
