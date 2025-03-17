import unittest

from src.domain.Movie import Movie
from src.repository.MovieRepository import MovieRepository
from src.repository.RepoException import RepoException


class TestMovieRepository(unittest.TestCase):
    def setUp(self):
        """Set up a new MovieRepository for each test."""
        self.repo = MovieRepository()
        self.movie1 = Movie(1, "Inception", "A mind-bending thriller", "Sci-Fi")
        self.movie2 = Movie(2, "Titanic", "A romantic tragedy", "Romance")
        self.movie3 = Movie(3, "The Matrix", "A hacker discovers reality", "Sci-Fi")

    def test_add_movie(self):
        """Test adding a movie to the repository."""
        self.repo.add_movie(self.movie1)
        self.assertEqual(len(self.repo.get_all_movies()), 1)
        self.assertEqual(self.repo.get_all_movies()[0].title, "Inception")

        with self.assertRaises(RepoException):
            self.repo.add_movie(self.movie1)

    def test_get_all_movies(self):
        """Test retrieving all movies from the repository."""
        self.repo.add_movie(self.movie1)
        self.repo.add_movie(self.movie2)
        movies = self.repo.get_all_movies()
        self.assertEqual(len(movies), 2)
        self.assertIn(self.movie1, movies)
        self.assertIn(self.movie2, movies)

    def test_get_movie_by_id(self):
        """Test retrieving a movie by its ID."""
        self.repo.add_movie(self.movie1)
        movie = self.repo.get_movie_by_id(1)
        self.assertEqual(movie.title, "Inception")

        self.assertIsNone(self.repo.get_movie_by_id(99))

    def test_delete_movie(self):
        """Test deleting a movie by its ID."""
        self.repo.add_movie(self.movie1)
        self.repo.add_movie(self.movie2)
        self.repo.delete_movie(1)
        self.assertEqual(len(self.repo.get_all_movies()), 1)
        self.assertNotIn(self.movie1, self.repo.get_all_movies())

        self.repo.delete_movie(99)
        self.assertEqual(len(self.repo.get_all_movies()), 1)

    def test_update_movie(self):
        """Test updating a movie's details."""
        self.repo.add_movie(self.movie1)
        updated_movie = Movie(1, "Inception 2", "A sequel to the mind-bending thriller", "Sci-Fi")
        self.repo.update_movie(updated_movie)
        movie = self.repo.get_movie_by_id(1)
        self.assertEqual(movie.title, "Inception 2")
        self.assertEqual(movie.description, "A sequel to the mind-bending thriller")
        self.assertEqual(movie.genre, "Sci-Fi")

