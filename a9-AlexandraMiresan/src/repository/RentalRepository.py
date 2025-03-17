from datetime import datetime

from src.repository.RepoException import RepoException


class RentalRepository:
    def __init__(self):
        self._rental_list = []

    def get_all_rentals(self):
        """return a list of all rentals"""
        return self._rental_list

    def rent_a_movie(self, rental):
        """creates a new rental"""
        self._rental_list.append(rental)

    def return_rental(self, rental_id):
        """modifies an existing rental by adding a return date"""
        if self._rental_list[rental_id].returned_date:
            raise RepoException("Item already returned")
        self._rental_list[rental_id].returned_date = datetime.today().date()

    def delete_rental(self, rental_id):
        """deletes an existing rental"""
        for rental in self._rental_list:
            if rental.rental_id == rental_id:
                self._rental_list.remove(rental)

