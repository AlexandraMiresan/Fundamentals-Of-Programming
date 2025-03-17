from src.domain.Book import Book
from src.repository.BookRepository import BookRepository


class TestInMemoryRepo:
    def __init__(self):
        self.__run_tests()

    def __run_tests(self):
        self.__test_add()
        self.__test_remove()
        self.__test_get_by_id()

    def __test_add(self):
        bookRepo = BookRepository()
        testBook = Book("11111111111","test","test")
        bookRepo.add_book(testBook)
        assert bookRepo.get_all()[0] == testBook

    def __test_remove(self):
        print("running test...")
        bookRepo = BookRepository()
        id_to_remove_by = "11111111111"
        testBook = Book(id_to_remove_by,"test","test")
        bookRepo.add_book(testBook)
        assert len(bookRepo.get_all()) == 1
        bookRepo.remove_by_isbn(id_to_remove_by)
        assert len(bookRepo.get_all()) == 0

    def __test_get_by_id(self):
        bookRepo = BookRepository()
        id_to_get_by = "11111111111"
        testBook = Book(id_to_get_by, "test", "test")
        bookRepo.add_book(testBook)
        assert bookRepo.get_by_id(id_to_get_by) == testBook


