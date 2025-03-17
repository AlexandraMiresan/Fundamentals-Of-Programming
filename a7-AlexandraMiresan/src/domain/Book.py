from src.domain import ValidatorException

class Book:
    def __init__(self, isbn: str, title: str, author: str):
        self._isbn = isbn
        self._title = title
        self._author = author

    def __str__(self):
        return "The book: " + self._title + " is written by " + self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

class BookValidator:
    @staticmethod
    def validate(book):
        if not isinstance(book, Book):
            raise TypeError("Book must be of type 'Book'")
        _errors = []
        if len(book.isbn.replace("-","" )) < 10 or len(book.isbn.replace("-", "")) > 13:
            _errors.append("Incorrect ISBN")
        if len(book.title) < 3:
            _errors.append("Book title is too short")
        if len(book.author) < 3:
            _errors.append("Book author is too short")
        if len(_errors) > 0:
            raise ValidatorException.ValidatorError(_errors)