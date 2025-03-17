import unittest
import os

from src.domain.Book import Book
from src.repository.PickleBookRepository import PickleBookRepository
from src.repository.IOException import IOException



class TestPickleBookRepository(unittest.TestCase):

    def setUp(self):
        self.test_file = "TEST"
        self.repo = PickleBookRepository(self.test_file)
        self.sample_book = Book("1234567890", "Sample Book","Author")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        self.repo.add_book(self.sample_book)
        # Check if the book is in the repository
        self.assertIn(self.sample_book, self.repo.get_all())

    def test_remove_book(self):
        self.repo.add_book(self.sample_book)
        self.repo.remove_by_isbn(self.sample_book.isbn)
        # Ensure the book is removed
        self.assertNotIn(self.sample_book, self.repo.get_all())

    def test_file_not_found(self):
        # Remove the test file if it exists
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        with self.assertRaises(IOException):
            PickleBookRepository(self.test_file)

    def test_empty_file(self):
        # Create an empty file
        with open(self.test_file, "wb"):
            pass
        repo = PickleBookRepository(self.test_file)
        self.assertEqual(repo.get_all(), [])

