from datetime import datetime
from random import random, randint

from src.Validators.ClientValidator import ClientValidator
from src.Validators.MovieValidator import MovieValidator
from src.Validators.UIException import UIException
from src.Validators.UIValidator import UIValidator
from src.Validators.ValidatorException import ValidatorError
from src.domain.Client import Client
from src.domain.IdGenerator import IdGenerator
from src.domain.Movie import Movie
from src.repository.RepoException import RepoException
from src.services.ClientService import ClientService
from src.services.MovieService import MovieService
from src.services.RentalService import RentalService
from src.services.ServiceException import ServiceException
from src.services.UndoService import UndoService, UndoError


class UI:
    def __init__(self, movie_repo, client_repo, rental_repo, undo_service, rental_service):
        self._movie_service = MovieService(movie_repo, rental_repo, undo_service, rental_service)
        self._client_service = ClientService(client_repo, rental_repo, undo_service, rental_service)
        self._rental_service = rental_service
        self._undo_service = undo_service

    def start_ui(self):
        while True:
            self.print_menu()
            choice = self.get_input()
            match choice:
                case '1':
                    self.add_movie()
                case '2':
                    self.add_client()
                case '3':
                    self.rent_a_movie()
                case '4':
                    self.show_all_movies()
                case '5':
                    self.show_all_clients()
                case '6':
                    self.show_all_rentals()
                case '7':
                    self.remove_movie()
                case '8':
                    self.remove_client()
                case '9':
                    self.return_movie()
                case '10':
                    self.update_movie()
                case '11':
                    self.update_client()
                case '12':
                    self.search_movie_by_id()
                case '13':
                    self.search_movie_by_title()
                case '14':
                    self.search_movie_by_genre()
                case '15':
                    self.search_movie_by_description()
                case '16':
                    self.search_clients_by_id()
                case '17':
                    self.search_clients_by_name()
                case '18':
                    self.undo_operation()
                case '19':
                    self.redo_operation()
                case '20':
                    self.most_rented_movies()
                case '21':
                    self.most_active_clients()
                case '22':
                    self.late_rentals()
                case '0':
                    break
                case default:
                    print("Please enter a valid choice")

    def print_menu(self):
        print("1. Add Movie")
        print("2. Add Client")
        print("3. Rent a movie")
        print("4. Show all movies")
        print("5. Show all clients")
        print("6. Show all rentals")
        print("7. Remove movie")
        print("8. Remove client")
        print("9. Return a movie")
        print("10. Update movie")
        print("11. Update client")
        print("12. Search movies by id")
        print("13. Search movies by title")
        print("14. Search movies by genre")
        print("15. Search movies by description")
        print("16. Search clients by id")
        print("17. Search clients by name")
        print("18. Undo")
        print("19. Redo")
        print("20. Most rented movies")
        print("21. Most active clients")
        print("22. Late rentals")
        print("0. Exit")

    def add_movie(self):
        try:
            movie = self.read_movie()
            self._movie_service.add_movie(movie)
            print("The movie has been successfully added.\n")
        except RepoException as e:
            print(e)

    def read_movie(self):
        try:
            title = input("Enter Movie Title: ")
            description = input("Enter Movie Description: ")
            genre = input("Enter Movie Genre: ")
            movie_id = IdGenerator.generate_unique_id()
            movie = Movie(movie_id, title, description, genre)
            MovieValidator.validate(movie)
            return movie
        except ValidatorError as e:
            print(e)
        except ValueError as t:
            print(t)

    def get_input(self):
        choice = input("Enter a choice: ")
        try:
            UIValidator.validate_input(choice)
            return choice
        except UIException as u:
            print(u)

    def add_client(self):
        try:
            client = self._read_client()
            self._client_service.add_client(client)
            print("The client has been successfully added.\n")
        except RepoException as e:
            print(e)
            
    def _read_client(self):
        try:
            name = input("Enter Client Name: ")
            client_id = randint(1, 9999)
            client = Client(client_id, name)
            ClientValidator.validate(client)
            return client
        except ValidatorError as e:
            print(e)

    def rent_a_movie(self):
        try:
            self.show_all_movies()
            movie_id = int(input("Enter Movie Id: "))
            self.show_all_clients()
            client_id = int(input("Enter Client Id: "))
            date = datetime.strptime(input("Enter due date after format month-day-year: "), '%m-%d-%Y').date()
            self._rental_service.rent_movie(movie_id, client_id, date)
        except ServiceException as e:
            print(e)
        except ValueError as e:
            print(e)

    def show_all_movies(self):
        for movie in self._movie_service.get_all_movies():
            print(movie)

    def show_all_clients(self):
        for client in self._client_service.get_all_clients():
            print(client)

    def show_all_rentals(self):
        index = 0
        for rental in self._rental_service.get_all_rentals():
            print(str(index) + ": " + str(rental))
            index += 1

    def _input_remove_movie(self):
        try:
            movie_id = int(input("Enter Movie ID: "))
            return movie_id
        except ValueError as e:
            print(e)

    def _input_remove_client(self):
        try:
            client_id = int(input("Enter Client ID: "))
            return client_id
        except ValueError as e:
            print(e)

    def remove_movie(self):
        movie_id = self._input_remove_movie()
        if not self._movie_service.get_by_id(movie_id):
            print("Id not found.")
            return

        self._movie_service.delete_movie(movie_id)
        print("The movie has been successfully removed.\n")

    def remove_client(self):
        client_id = self._input_remove_client()
        if not self._client_service.get_by_id(client_id):
            print("Id not found.")
            return

        self._client_service.delete_client(client_id)
        print("The client has been successfully removed.\n")

    def return_movie(self):
        self.show_all_rentals()
        try:
            choice = int(input("Choose rental: "))
            if choice < 0  or choice >= len(self._rental_service.get_all_rentals()):
                print("Invalid choice.")
                return
            rental_id = self._rental_service.get_all_rentals()[choice].rental_id
            self._rental_service.return_movie(choice)
        except ValueError as e:
            print(e)
        except RepoException as e:
            print(e)

    def _input_update_movie(self):
        try:
            movie_id = int(input("Enter Movie ID: "))
            title = input("Enter Movie Title: ")
            description = input("Enter Movie Description: ")
            genre = input("Enter Movie Genre: ")
            movie = Movie(movie_id, title, description, genre)
            MovieValidator.validate(movie)
            return movie
        except ValidatorError as e:
            print(e)

    def update_movie(self):
        movie = self._input_update_movie()
        if not self._movie_service.get_by_id(movie.movie_id):
            print("Id not found.")
            return
        self._movie_service.update_movie(movie)
        print("The movie has been successfully updated.\n")

    def _input_update_client(self):
        try:
            client_id = int(input("Enter Client ID: "))
            name = input("Enter Client Name: ")
            client = Client(client_id, name)
            ClientValidator.validate(client)
            return client
        except ValidatorError as e:
            print(e)

    def update_client(self):
        client = self._input_update_client()
        if not self._client_service.get_by_id(client.client_id):
            print("Id not found.")
            return
        self._client_service.update_client(client)
        print("The client has been successfully updated.\n")

    def search_movie_by_id(self):
        user_input = input("Enter Movie ID: ")
        for movie in self._movie_service.search_movies_by_id(user_input):
            print(movie)

    def search_movie_by_title(self):
        user_input = input("Enter Movie Title: ")
        for movie in self._movie_service.search_movies_by_title(user_input):
            print(movie)

    def search_movie_by_genre(self):
        user_input = input("Enter Movie Genre: ")
        for movie in self._movie_service.search_movies_by_genre(user_input):
            print(movie)

    def search_movie_by_description(self):
        user_input = input("Enter Movie Description: ")
        for movie in self._movie_service.search_movies_by_description(user_input):
            print(movie)

    def search_clients_by_id(self):
        user_input = input("Enter Client ID: ")
        for client in self._client_service.search_clients_by_id(user_input):
            print(client)

    def search_clients_by_name(self):
        user_input = input("Enter Client Name: ")
        for client in self._client_service.search_clients_by_name(user_input):
            print(client)

    def undo_operation(self):
        try:
            self._undo_service.undo()
            print("Undo operation has been successful.")
        except UndoError as e:
            print(e)

    def redo_operation(self):
        try:
            self._undo_service.redo()
            print("Redo operation has been successful.")
        except UndoError as e:
            print(e)

    def most_rented_movies(self):
        result = self._rental_service.most_rented_movies()
        for movie in result:
            print(movie)

    def most_active_clients(self):
        result = self._rental_service.most_active_clients()
        for client in result:
            print(client)

    def late_rentals(self):
        result = self._rental_service.late_rentals()
        for movie in result:
            print(movie)







