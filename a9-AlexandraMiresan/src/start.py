from src.generateValues.ClientGenerator import ClientGenerator
from src.generateValues.MovieGenerator import MovieGenerator
from src.generateValues.RentalGenerator import RentalGenerator
from src.repository.ClientRepository import ClientRepository
from src.repository.MovieRepository import MovieRepository
from src.repository.PickleClientRepository import PickleClientRepository
from src.repository.PickleMovieRepository import PickleMovieRepository
from src.repository.PickleRentalRepository import PickleRentalRepository
from src.repository.RentalRepository import RentalRepository
from src.repository.TextFileClientRepository import TextFileClientRepository
from src.repository.TextFileMovieRepository import TextFileMovieRepository
from src.repository.TextFileRentalRepository import TextFileRentalRepository
from src.services.RentalService import RentalService
from src.services.UndoService import UndoService
from src.tests.TestClientRepo import TestClientRepository
from src.tests.TestClientService import TestClientService
from src.tests.TestMovieRepo import TestMovieRepository
from src.tests.TestMovieService import TestMovieService
from src.tests.TestRentalRepo import TestRentalRepository
from src.tests.TestRentalService import TestRentalService
from src.ui.UI import UI


def populate_movies_repository(movie_repo):
    movie_generator = MovieGenerator()
    for movies in range(1, 21):
        movie = movie_generator.generate_valid_movie()
        movie_repo.add_movie(movie)

def populate_rental(rental_repo, movies_list, client_list):
    rental_generator = RentalGenerator()
    for rentals in range(1,21):
        rental = rental_generator.generate_valid_rental(movies_list, client_list)
        rental_repo.rent_a_movie(rental)

def populate_client_repository(client_repo):
    client_generator = ClientGenerator()
    for clients in range(1, 21):
        client_repo.add_client(client_generator.generate_valid_client())

def main():
    file = open("settings.properties", "rt")
    repo_type = file.readline().split("=")[1].replace("\n", "")
    movie_repo_file = file.readline().split("=")[1].replace("\"", "").replace("\n", "")
    client_repo_file = file.readline().split("=")[1].replace("\"", "").replace("\n", "")
    rental_repo_file = file.readline().split("=")[1].replace("\"", "").replace("\n", "")

    match repo_type:
        case "inmemory":
            movie_repo = MovieRepository()
            populate_movies_repository(movie_repo)
            client_repo = ClientRepository()
            populate_client_repository(client_repo)
            rental_repo = RentalRepository()
            undo_service = UndoService()
            rental_service = RentalService(rental_repo, movie_repo, client_repo, undo_service)
            populate_rental(rental_repo, movie_repo.get_all_movies(), client_repo.get_all_clients())
            ui = UI(movie_repo, client_repo, rental_repo, undo_service, rental_service)
        case "textfiles":
            ui = UI(TextFileMovieRepository(movie_repo_file), TextFileClientRepository(client_repo_file), TextFileRentalRepository(rental_repo_file), undo_service, rental_service)
        case "binaryfiles":
            ui = UI(PickleMovieRepository(movie_repo_file), PickleClientRepository(client_repo_file),PickleRentalRepository(rental_repo_file))
        case default:
            return
    ui.start_ui()

def tests():
    testmovierepo = TestMovieRepository()
    testclientrepo = TestClientRepository()
    testrentalrepo = TestRentalRepository()
    testmovieserv = TestMovieService()
    testclientserv = TestClientService()
    testrentalserv = TestRentalService()

if __name__ == "__main__":
    main()
    tests()