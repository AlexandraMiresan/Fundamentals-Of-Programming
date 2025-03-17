import unittest
from unittest.mock import MagicMock

from src.domain.Movie import Movie
from src.domain.Rental import Rental
from src.services.MovieService import MovieService

class TestMovieService(unittest.TestCase):
    def setUp(self):
        """Set up mock repositories and service for each test."""
        self.mock_movie_repo = MagicMock()
        self.mock_rental_repo = MagicMock()
        self.service = MovieService(self.mock_movie_repo, self.mock_rental_repo)

        self.movie1 = Movie(1, "Inception", "A mind-bending thriller", "Sci-Fi")
        self.movie2 = Movie(2, "Titanic", "A tragic love story", "Romance")
        self.movie3 = Movie(3, "The Matrix", "A hacker discovers the truth", "Sci-Fi")

        self.rental1 = Rental(1, 101, 1, "2024-01-01")
        self.rental2 = Rental(2, 102, 2, "2024-01-05")

    def test_add_movie(self):
        """Test adding a movie through the service."""
        self.service.add_movie(self.movie1)
        self.mock_movie_repo.add_movie.assert_called_once_with(self.movie1)

    def test_get_all_movies(self):
        """Test retrieving all movies through the service."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2]
        movies = self.service.get_all_movies()
        self.assertEqual(len(movies), 2)
        self.assertIn(self.movie1, movies)
        self.assertIn(self.movie2, movies)

    def test_search_movies_by_title(self):
        """Test searching for movies by title."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2, self.movie3]
        result = self.service.search_movies_by_title("Inception")
        self.assertEqual(len(result), 1)
        self.assertIn(self.movie1, result)

    def test_search_movies_by_id(self):
        """Test searching for movies by ID."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2]
        result = self.service.search_movies_by_id("1")
        self.assertEqual(len(result), 1)
        self.assertIn(self.movie1, result)

    def test_search_movies_by_genre(self):
        """Test searching for movies by genre."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2, self.movie3]
        result = self.service.search_movies_by_genre("Sci-Fi")
        self.assertEqual(len(result), 2)
        self.assertIn(self.movie1, result)
        self.assertIn(self.movie3, result)

    def test_search_movies_by_description(self):
        """Test searching for movies by description."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2]
        result = self.service.search_movies_by_description("mind-bending")
        self.assertEqual(len(result), 1)
        self.assertIn(self.movie1, result)

    def test_update_movie(self):
        """Test updating a movie through the service."""
        updated_movie = Movie(1, "Inception", "A sci-fi masterpiece", "Sci-Fi")
        self.service.update_movie(updated_movie)
        self.mock_movie_repo.update_movie.assert_called_once_with(updated_movie)

    def test_delete_movie(self):
        """Test deleting a movie through the service."""
        self.mock_rental_repo.get_all_rentals.return_value = [self.rental1, self.rental2]
        self.service.delete_movie(1)
        self.mock_movie_repo.delete_movie.assert_called_once_with(1)
        self.mock_rental_repo.delete_rental.assert_called_once_with(1)

    def test_get_by_id(self):
        """Test retrieving a movie by ID."""
        self.mock_movie_repo.get_all_movies.return_value = [self.movie1, self.movie2]
        movie = self.service.get_by_id(1)
        self.assertEqual(movie, self.movie1)

