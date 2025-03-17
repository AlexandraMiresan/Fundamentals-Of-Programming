import unittest

from Domain.board import Board
from Repository.Repository import Repository
from Service.ComputerPlayerService import Bot
from Service.GameException import GameError
from Service.GameService import GameService
from Service.Validator import Validator


class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.repo = Repository(self.board)
        self.validator = Validator()
        self.service = GameService(self.repo, self.validator)

    def test_check_win_straight_line(self):
        self.board.Clear_board()
        self.repo.update(1, 0, " ◯ ")
        self.repo.update(2, 0, " ◯ ")
        self.repo.update(3, 0, " ◯ ")
        self.repo.update(4, 0, " ◯ ")
        self.assertTrue(self.service.check_win(0, 1, " ◯ "))
        self.assertTrue(self.service.check_win(0, 4, " ◯ "))

    def test_check_win_vertical_line(self):
        self.board.Clear_board()
        self.repo.update(0, 0, " ◯ ")
        self.repo.update(0, 1, " ◯ ")
        self.repo.update(0, 2, " ◯ ")
        self.repo.update(0, 3, " ◯ ")
        self.assertTrue(self.service.check_win(0, 0, " ◯ "))
        self.assertTrue(self.service.check_win(3, 0, " ◯ "))

    def test_check_win_diagonal_line_right(self):
        self.board.Clear_board()
        self.repo.update(0, 0, " ◯ ")
        self.repo.update(1, 1, " ◯ ")
        self.repo.update(2, 2, " ◯ ")
        self.repo.update(3, 3, " ◯ ")
        self.assertTrue(self.service.check_win(0, 0, " ◯ "))
        self.assertTrue(self.service.check_win(3, 3, " ◯ "))

    def test_check_win_diagonal_line_left(self):
        self.board.Clear_board()
        self.repo.update(0, 3, " ◯ ")
        self.repo.update(1, 2, " ◯ ")
        self.repo.update(2, 1, " ◯ ")
        self.repo.update(3, 0, " ◯ ")
        self.assertTrue(self.service.check_win(0, 3, " ◯ "))
        self.assertTrue(self.service.check_win(3, 0, " ◯ "))

    def test_win_false(self):
        self.board.Clear_board()
        self.repo.update(0, 3, " ◯ ")
        self.repo.update(1, 2, " ◯ ")
        self.repo.update(2, 1, " ◯ ")
        self.assertFalse(self.service.check_win(3, 0, " ◯ "))
        self.assertFalse(self.service.check_win(5, 5, " ◯ "))

    def test_check_board_state_win_and_lose(self):
        self.board.Clear_board()
        self.repo.update(1, 0, " ◯ ")
        self.repo.update(2, 0, " ◯ ")
        self.repo.update(3, 0, " ◯ ")
        self.assertFalse(self.service.check_board_state(" ◯ "))
        self.repo.update(4, 0, " ◯ ")
        self.assertTrue(self.service.check_board_state(" ◯ "))

    def test_play_piece(self):
        self.service.play_piece(6, " ◯ ")
        self.assertEqual(self.board.board[5][5], " ◯ ")
        self.service.play_piece(6, " ◯ ")
        self.service.play_piece(6, " ◯ ")
        self.service.play_piece(6, " ◯ ")
        self.service.play_piece(6, " ◯ ")
        self.service.play_piece(6, " ◯ ")
        self.assertRaises(GameError, self.service.play_piece, 6, " ◯ ")

    def test_validate(self):
        self.assertRaises(GameError, self.service.play_piece, "idk", " ◯ ")
        self.assertRaises(GameError, self.service.play_piece, 10, " ◯ ")

    def test_str(self):
        self.assertEqual(str(self.service), "|	,	,	,	,	,	,	,|\n|	,	,	,	,	,	,	,|\n"
                                            "|	,	,	,	,	,	,	,|\n|	,	,	,	,	,	,	,|\n|"
                                            "	,	,	,	,	,	,	,|\n|	,	,	,	,	,	,	,|\n")

    def tearDown(self):
        self.board = None
        self.repo = None
        self.service = None


class TestBOTService(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.repo = Repository(self.board)
        self.validator = Validator()
        self.service = GameService(self.repo, self.validator)
        self.bot_service = Bot(self.service, self.repo)

    def test_check_player_about_to_win_horizontally(self):
        self.repo.update(1, 5, " ◯ ")
        self.repo.update(2, 5, " ◯ ")
        self.repo.update(3, 5, " ◯ ")
        self.assertEqual((5,0),self.bot_service.check_player_about_to_win(" ◯ "))
        self.board.Clear_board()
        self.repo.update(0, 5, " ◯ ")
        self.repo.update(1, 5, " ◯ ")
        self.repo.update(2, 5, " ◯ ")
        self.assertEqual((5, 3), self.bot_service.check_player_about_to_win(" ◯ "))
        self.board.Clear_board()
        self.repo.update(6, 4, " ◯ ")
        self.repo.update(5, 4, " ◯ ")
        self.repo.update(4, 4, " ◯ ")
        self.repo.update(3, 3, ' ◍ ')
        self.repo.update(3, 2, ' ◍ ')
        self.repo.update(3, 1, ' ◍ ')
        self.repo.update(3, 0, ' ◍ ')
        #self.assertEqual((4, 3), self.bot_service.check_player_about_to_win(" ◯ "))

    def test_check_player_about_to_win_vertically(self):
        self.board.Clear_board()
        self.repo.update(0, 5, " ◯ ")
        self.repo.update(0, 4, " ◯ ")
        self.repo.update(0, 3, " ◯ ")
        self.assertEqual((2, 0), self.bot_service.check_player_about_to_win(" ◯ "))

    def test_check_player_about_to_win_diagonally(self):
        self.board.Clear_board()
        self.repo.update(0, 5, " ◯ ")
        self.repo.update(1, 4, " ◯ ")
        self.repo.update(2, 3, " ◯ ")
        self.repo.update(3, 5, ' ◍ ')
        self.repo.update(3, 4, ' ◍ ')
        self.repo.update(3, 3, ' ◍ ')
        self.assertEqual((2, 3), self.bot_service.check_player_about_to_win(" ◯ "))
        self.board.Clear_board()
        self.repo.update(5, 5, " ◯ ")
        self.repo.update(4, 4, " ◯ ")
        self.repo.update(3, 3, " ◯ ")
        self.repo.update(2, 5, ' ◍ ')
        self.repo.update(2, 4, ' ◍ ')
        self.repo.update(2, 3, ' ◍ ')
        self.assertEqual((2, 2), self.bot_service.check_player_about_to_win(" ◯ "))
        self.board.Clear_board()
        self.repo.update(3, 3, " ◯ ")
        self.repo.update(2, 2, " ◯ ")
        self.repo.update(1, 1, " ◯ ")
        #self.assertEqual((0, 0), self.bot_service.check_player_about_to_win(" ◯ "))

    def test_make_a_play(self):
        self.bot_service.make_a_play(2)
        self.board.Clear_board()
        self.repo.update(1, 5, ' ◍ ')
        self.repo.update(2, 5, ' ◍ ')
        self.repo.update(3, 5, ' ◍ ')
        self.assertEqual("Computer wins!",self.bot_service.make_a_play(4))
        self.board.Clear_board()
        self.repo.update(1, 5, ' ◍ ')
        self.repo.update(2, 5, ' ◍ ')
        self.assertEqual(None, self.bot_service.make_a_play(4))
        self.board.Clear_board()
        self.repo.update(0, 5, " ◯ ")
        self.repo.update(1, 5, " ◯ ")
        self.repo.update(2, 5, " ◯ ")
        self.assertEqual(None, self.bot_service.make_a_play(4))


    def test_check_player_about_to_win_false(self):
        self.board.Clear_board()
        self.assertEqual((-1,-1),self.bot_service.check_player_about_to_win(" ◯ "))

    def tearDown(self):
        self.board = None
        self.repo = None
        self.validator = None
        self.service = None
        self.bot_service = None

class TestGameError(unittest.TestCase):
    def setUp(self):
        self._message = GameError(["idk"])

    def test_str(self):
        self.assertEqual(str(self._message), "idk\n")

    def tearDown(self):
        self._message = None