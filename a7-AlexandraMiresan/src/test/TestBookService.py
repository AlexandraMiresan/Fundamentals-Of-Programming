from src import repository
from src.repository.BookRepository import BookRepository
from src.services.BookService import BookService


class TestBookService:
    def __init__(self):
        self.__run_tests()
        self._repository = BookRepository()

    def __run_tests(self):
        self.__test_add()

    def __test_add(self):
        self._book_service = BookService("IN_MEMORY")
        BookService.add_book(self._book_service, "1234567890", "test", "test")
        assert BookService.get_all_books(self._book_service) [10].isbn == "1234567890"