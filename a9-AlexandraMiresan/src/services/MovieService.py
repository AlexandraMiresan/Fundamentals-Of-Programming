from src.generateValues.MovieGenerator import MovieGenerator
from src.services.UndoService import FunctionCall, Operation, CascadedOperation


class MovieService:
    def __init__(self, movie_repo, rental_repo, undo_service, rental_service):
        self._movie_repository = movie_repo
        self._rental_repository = rental_repo
        self._undo_service = undo_service
        self._rental_service = rental_service

    def get_repo(self):
        return self._movie_repository

    def set_repo(self, repo):
        self._movie_repository = repo

    def add_movie(self, movie):
        self._movie_repository.add_movie(movie)

        functionRedo = FunctionCall(self._movie_repository.add_movie, movie)
        functionUndo = FunctionCall(self._movie_repository.delete_movie, movie.movie_id)

        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))


    def get_all_movies(self):
        return self._movie_repository.get_all_movies()

    def search_movies_by_title(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for movie in self._movie_repository.get_all_movies():
            if movie.title.lower() == user_input:
                new_list.append(movie)
            elif user_input in movie.title:
                new_list.append(movie)
        return new_list

    def search_movies_by_id(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for movie in self._movie_repository.get_all_movies():
            if movie.movie_id == user_input:
                new_list.append(movie)
            elif user_input in str(movie.movie_id):
                new_list.append(movie)
        return new_list

    def search_movies_by_genre(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for movie in self._movie_repository.get_all_movies():
            if movie.genre.lower() == user_input:
                new_list.append(movie)
            elif user_input in movie.genre.lower():
                new_list.append(movie)
        return new_list

    def search_movies_by_description(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for movie in self._movie_repository.get_all_movies():
            if movie.description.lower() == user_input:
                new_list.append(movie)
            elif user_input in movie.description:
                new_list.append(movie)
        return new_list

    def update_movie(self, movie_to_update):
        movie = self._movie_repository.update_movie(movie_to_update)
        self._movie_repository.update_movie(movie)
        functionRedo = FunctionCall(self._movie_repository.update_movie, movie_to_update)
        functionUndo = FunctionCall(self._movie_repository.update_movie, movie)
        operation = [Operation(functionUndo, functionRedo)]

        self._undo_service.recordUndo(operation)

        return movie

    def delete_movie(self, movie_id):
        movie = self._movie_repository.get_movie_by_id(movie_id)
        self._movie_repository.delete_movie(movie_id)
        rentalRepo = self._rental_repository.get_all_rentals().copy()
        for rental in self._rental_repository.get_all_rentals():
            if movie.movie_id == rental.movie_id:
             self._rental_repository.delete_rental(rental.rental_id)

        functionRedo = FunctionCall(self._movie_repository.delete_movie, movie.movie_id)
        functionUndo = FunctionCall(self._movie_repository.add_movie, movie)
        operations = [Operation(functionUndo, functionRedo)]

        for rental in rentalRepo:
            if movie.movie_id == rental.movie_id:
                functionRedo = FunctionCall(self._rental_repository.delete_rental, rental.rental_id)
                functionUndo = FunctionCall(self._rental_repository.rent_a_movie, rental)

                operations.append(Operation(functionUndo, functionRedo))

        self._undo_service.recordUndo(CascadedOperation(*operations))

    def get_by_id(self, movie_id):
        for movie in self._movie_repository.get_all_movies():
            if movie.movie_id == movie_id:
                return movie