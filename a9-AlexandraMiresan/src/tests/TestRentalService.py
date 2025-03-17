import unittest
from unittest.mock import MagicMock
from datetime import datetime

from src.domain.Client import Client
from src.domain.Movie import Movie
from src.domain.Rental import Rental
from src.services.RentalService import RentalService
from src.services.ServiceException import ServiceException


class TestRentalService(unittest.TestCase):
    def setUp(self):
        """Set up mock repositories and service for each test."""
        self.mock_rental_repo = MagicMock()
        self.mock_movie_repo = MagicMock()
        self.mock_client_repo = MagicMock()
        self.service = RentalService(self.mock_rental_repo, self.mock_movie_repo, self.mock_client_repo)

        self.client1 = Client(1, "Alice")
        self.client2 = Client(2, "Bob")

        self.movie1 = Movie(1, "Inception", "A mind-bending thriller", "Sci-Fi")
        self.movie2 = Movie(2, "Titanic", "A tragic love story", "Romance")

        today = datetime.today().date()
        self.rental1 = Rental(1, 1, 1, today.replace(day=today.day - 10), today.replace(day=today.day - 5))
        self.rental2 = Rental(2, 2, 2, today, today.replace(day=today.day + 5))

    def test_check_if_client_has_rented(self):
        """Test if the client has rentals that are overdue."""
        self.mock_rental_repo.get_all_rentals.return_value = [self.rental1, self.rental2]
        result = self.service.check_if_client_has_rented(1)
        self.assertTrue(result)

    def test_check_if_client_exists(self):
        """Test if a client exists in the repository."""
        self.mock_client_repo.get_all_clients.return_value = [self.client1, self.client2]
        result = self.service.check_if_client_exists(1)
        self.assertTrue(result)

        result = self.service.check_if_client_exists(3)
        self.assertFalse(result)

    def test_check_if_movie_exists(self):
        """Test if a movie exists in the repository."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2]
        result = self.service.check_if_movie_exists(1)
        self.assertTrue(result)

        result = self.service.check_if_movie_exists(3)
        self.assertFalse(result)

    def test_rent_movie(self):
        """Test renting a movie through the service."""
        self.mock_client_repo.get_client_by_id.return_value = self.client1
        self.mock_movie_repo.get_movie_by_id.return_value = self.movie1
        self.mock_rental_repo.get_all_rentals.return_value = []

        future_date = datetime.today().date().replace(day=datetime.today().date().day + 5)
        self.service.rent_movie(1, 1, future_date)
        self.mock_rental_repo.rent_a_movie.assert_called_once()

    def test_rent_movie_invalid_client(self):
        """Test renting a movie with an invalid client."""
        self.mock_client_repo.get_client_by_id.return_value = None
        future_date = datetime.today().date().replace(day=datetime.today().date().day + 5)

        with self.assertRaises(ServiceException):
            self.service.rent_movie(1, 1, future_date)

    def test_rent_movie_overdue_rental(self):
        """Test renting a movie when the client has an overdue rental."""
        self.mock_client_repo.get_client_by_id.return_value = self.client1
        self.mock_movie_repo.get_movie_by_id.return_value = self.movie1
        today = datetime.today().date()
        overdue_rental = Rental(3, 1, 3, today.replace(day=today.day - 20), today.replace(day=today.day - 10), None)
        self.mock_rental_repo.get_all_rentals.return_value = [overdue_rental]

        future_date = today.replace(day=today.day + 5)
        with self.assertRaises(ServiceException):
            self.service.rent_movie(1, 1, future_date)

    def test_rent_movie_invalid_due_date(self):
        """Test renting a movie with a due date in the past."""
        self.mock_client_repo.get_client_by_id.return_value = self.client1
        self.mock_movie_repo.get_movie_by_id.return_value = self.movie1
        self.mock_rental_repo.get_all_rentals.return_value = []

        past_date = datetime.today().date().replace(day=datetime.today().date().day - 1)
        with self.assertRaises(ServiceException):
            self.service.rent_movie(1, 1, past_date)

    def test_return_movie(self):
        """Test returning a rented movie."""
        self.service.return_movie(1)
        self.mock_rental_repo.return_rental.assert_called_once_with(1)

    def test_get_all_rentals(self):
        """Test retrieving all rentals."""
        self.mock_rental_repo.get_all_rentals.return_value = [self.rental1, self.rental2]
        rentals = self.service.get_all_rentals()
        self.assertEqual(len(rentals), 2)
        self.assertIn(self.rental1, rentals)
        self.assertIn(self.rental2, rentals)
