from datetime import datetime, date


class Rental:
    def __init__(self, rental_id: int, movie_id: int, client_id: int, rented_date: date, due_date: date, returned_date: date):
        self._rental_id = rental_id
        self._movie_id = movie_id
        self._client_id = client_id
        self._rented_date = rented_date
        self._due_date = due_date
        self._returned_date = returned_date

    def __str__(self):
        return ("The id of the rented movie is: " + str(self.movie_id) + " , rented by client " + str(self.client_id) + " from "
                + str(self.rented_date) + " to " + str(self.due_date) + "." + " It has been returned on " + str(self.returned_date))

    @property
    def rental_id(self):
        return self._rental_id

    @property
    def movie_id(self):
        return self._movie_id

    @property
    def client_id(self):
        return self._client_id

    @property
    def rented_date(self):
        return self._rented_date

    @property
    def due_date(self):
        return self._due_date

    @property
    def returned_date(self):
        return self._returned_date

    @returned_date.setter
    def returned_date(self, value):
        self._returned_date = value