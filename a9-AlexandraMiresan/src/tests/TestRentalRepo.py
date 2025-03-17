import unittest
from datetime import datetime, timedelta

from src.domain.Rental import Rental
from src.repository.RentalRepository import RentalRepository
from src.repository.RepoException import RepoException


class TestRentalRepository(unittest.TestCase):
    def setUp(self):
        """Set up a new RentalRepository for each test."""
        self.repo = RentalRepository()
        self.rental1 = Rental(1, 101, 201, datetime(2024, 1, 1))
        self.rental2 = Rental(2, 102, 202, datetime(2024, 1, 5))

    def test_get_all_rentals(self):
        """Test retrieving all rentals from the repository."""
        self.repo.rent_a_movie(self.rental1)
        self.repo.rent_a_movie(self.rental2)
        rentals = self.repo.get_all_rentals()
        self.assertEqual(len(rentals), 2)
        self.assertIn(self.rental1, rentals)
        self.assertIn(self.rental2, rentals)

    def test_rent_a_movie(self):
        """Test adding a new rental to the repository."""
        self.repo.rent_a_movie(self.rental1)
        self.assertEqual(len(self.repo.get_all_rentals()), 1)
        self.assertEqual(self.repo.get_all_rentals()[0].client_id, 101)

    def test_return_rental(self):
        """Test modifying a rental to add a return date."""
        self.repo.rent_a_movie(self.rental1)
        self.repo.return_rental(0)
        rental = self.repo.get_all_rentals()[0]
        self.assertIsNotNone(rental.returned_date)
        self.assertEqual(rental.returned_date, datetime.today().date())


        with self.assertRaises(RepoException):
            self.repo.return_rental(0)

    def test_delete_rental(self):
        """Test deleting a rental by its ID."""
        self.repo.rent_a_movie(self.rental1)
        self.repo.rent_a_movie(self.rental2)
        self.repo.delete_rental(1)
        rentals = self.repo.get_all_rentals()
        self.assertEqual(len(rentals), 1)
        self.assertNotIn(self.rental1, rentals)
        self.repo.delete_rental(99)
        self.assertEqual(len(rentals), 1)

