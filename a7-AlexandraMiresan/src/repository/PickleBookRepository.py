import pickle

from src.repository.BookRepository import BookRepository
from src.repository.IOException import IOException



class PickleBookRepository(BookRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            file = open(file_name, "rb")
            self._book_list = pickle.load(file)
            file.close()
        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def add_book(self, book_to_add):
        super().add_book(book_to_add)
        self.__save_file()

    def __save_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self._book_list, file)
        file.close()

    def refresh(self):
        self.__save_file()

    def remove_by_isbn(self, isbn):
        super().remove_by_isbn(isbn)
        self.__save_file()
