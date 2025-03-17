from src.domain.Book import Book
from src.repository import BookRepository
from src.repository.BookRepository import BookRepository
from src.repository.PickleBookRepository import PickleBookRepository
from src.repository.TextFileBookRepository import TextFileBookRepository


class BookService:
    def __init__(self, option_of_repository: str):
        match option_of_repository:
            case "IN_MEMORY":
                self._repository = BookRepository()
                self.__populate_book_repo()
            case "TEXTFILE":
                self._repository = TextFileBookRepository("books.txt")
            case "PICKLE":
                self._repository = PickleBookRepository("PICKLE")
            case default:
                self._repository = BookRepository()
                self.__populate_book_repo()

    def add_book(self, isbn, title, author):
        """
        adds a new book to the repository
        :param isbn:
        :param title:
        :param author:
        :return:
        """
        book = Book(isbn, title, author)
        self._repository.add_book(book)

    def get_all_books(self):
        return self._repository.get_all()

    def filter_books_based_on_title(self, title: str):
        for book in self._repository.get_all().copy():
            if book.title.startswith(title):
                self._repository.remove_by_isbn(book.isbn)

    def get_repo(self):
        return self._repository

    def set_repo(self, repo):
        self._repository = repo

    def __populate_book_repo(self):
        self.add_book("11111111111","name1","name2")
        self.add_book("22222222222", "name2", "name2")
        self.add_book("33333333333", "name3", "name2")
        self.add_book("44444444444", "name4", "name2")
        self.add_book("55555555555", "name9", "name2")
        self.add_book("66666666666", "name6", "name2")
        self.add_book("77777777777","name5","name2")
        self.add_book("88888888888", "name8", "name2")
        self.add_book("99999999999","name7","name2")
        self.add_book("00000000000","name10","name2")

    def refreshFile(self):
        self._repository.refresh()

