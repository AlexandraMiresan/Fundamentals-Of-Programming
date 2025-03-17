from src.domain.Book import Book
from src.repository.BookRepository import BookRepository
from src.repository.IOException import IOException


class TextFileBookRepository(BookRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            fin = open(file_name, "rt")
            line = fin.readline()
            while len(line) > 0:
                tokens = line.split("|")
                super().add_book(Book(tokens[0], tokens[1], str(tokens[2]).strip()))
                line = fin.readline()
            fin.close()
        except FileNotFoundError:
            raise IOException("File not found")


    def add_book(self, book: Book):
        super().add_book(book)
        self.__save_file()

    def __save_file(self):
        fout = open(self._file_name, "wt")
        for book in self.get_all():
            fout.write(str(book.isbn) + "|" + str(book.title) + "|" + str(book.author) + "\n")
        fout.close()

    def remove_by_isbn(self, isbn):
        super().remove_by_isbn(isbn)
        self.__save_file()

    def refresh(self):
        self.__save_file()
