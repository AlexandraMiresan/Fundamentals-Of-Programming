import copy

from src.services.BookService import BookService
from src.services.BookServiceException import BookServiceException
from src.services.UndoService import UndoService
from src.ui.UIException import UIException
from src.ui.UIValidator import UIValidator


class UI:
    def __init__(self, repo_type):
        self._book_service = BookService(repo_type)
        self._undo_service = UndoService()

    def start_ui(self):
        self._undo_service.save_history(copy.deepcopy(self._book_service.get_repo()))

        while True:
            self.print_menu()
            choice = self.get_input()
            match choice:
                case 1:
                    self.add_book()
                case 2:
                    self.display_booksies()
                case 3:
                    self.filter_books_by_title()
                    self.display_booksies()
                case 4:
                    self.undo()
                    self._book_service.refreshFile()
                case 0:
                    break
                case default:
                    print("Please enter a valid choice.")

    def undo(self):
        try:
            self._book_service.set_repo(self._undo_service.pop_history())
        except BookServiceException as be:
            print(be)

    def filter_books_by_title(self):
        title = input("Please enter title: ")
        self._undo_service.save_history(copy.deepcopy(self._book_service.get_repo()))
        self._book_service.filter_books_based_on_title(title)

    def display_booksies(self):
        for book in self._book_service.get_all_books():
            print(book)

    def add_book(self):
        (isbn, title, author) = self.read_book()
        try:
            self._undo_service.save_history(copy.deepcopy(self._book_service.get_repo()))
            self._book_service.add_book(isbn, title, author)
            print("The book was successfully added.")
            print()
        except Exception as e:
            print(e)

    def get_input(self):
        choice = input("Please enter a choice: ")
        try:
            UIValidator.validate_input(choice)
            return int(choice)
        except UIException as u:
            print(u)

    def read_book(self):
        isbn = input("Please enter ISBN: ")
        title = input("Please enter title: ")
        author = input("Please enter author: ")
        return isbn, title, author

    def print_menu(self):
        print("1. Add book.")
        print("2. Display booksies.")
        print("3. Filter books by title.")
        print("4. Undo.")
        print("0. Exit")
