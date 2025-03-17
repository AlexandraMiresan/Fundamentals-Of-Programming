from src.domain.Book import BookValidator
from src.repository.RepoException import RepoException


class BookRepository:
    def __init__(self):
        self._book_list = []

    def get_all(self):
        return self._book_list

    def get_by_id(self, isbn):
        for book in self._book_list:
            if book.isbn == isbn:
                return book

    def remove_by_isbn(self, isbn):
        for book in self._book_list:
            if book.isbn == isbn:
                self._book_list.remove(book)
                return True
        return False

    def add_book(self, book_to_add):

        BookValidator.validate(book_to_add)
        for book in self._book_list:
            if book.isbn == book_to_add.isbn:
                raise RepoException(["Book already exists"])

        self._book_list.append(book_to_add)

    def refresh(self):
        pass


