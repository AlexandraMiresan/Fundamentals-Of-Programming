import unittest
import os
from src.domain.Book import Book
from src.repository.TextFileBookRepository import TextFileBookRepository
from src.repository.IOException import IOException


class TestTextFileBookRepository(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        with open(self.test_file, "wt") as f:
            f.write("123|Sample Book|Author\n")
        self.repo = TextFileBookRepository(self.test_file)
        self.sample_book = Book("4567890123", "Another Book", "Another Author")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_file(self):
        books = self.repo.get_all()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].isbn, "1234567890")
        self.assertEqual(books[0].title, "Sample Book")
        self.assertEqual(books[0].author, "Author")

    def test_add_book(self):
        self.repo.add_book(self.sample_book)
        books = self.repo.get_all()
        self.assertIn(self.sample_book, books)

    def test_remove_book(self):
        self.repo.add_book(self.sample_book)
        self.repo.remove_by_isbn(self.sample_book.isbn)
        books = self.repo.get_all()
        self.assertNotIn(self.sample_book, books)

    def test_file_not_found(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        with self.assertRaises(IOException):
            TextFileBookRepository(self.test_file)





