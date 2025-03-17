import unittest

from domain.Board import Board
from service.Service import Service


class Tests(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._service = Service(self._board)


    def test_attack(self):
        row = 1
        col = "C"
        assert self._service.attack_square(row, col, enemies = 1) == ("You missed!", 1)

        row = 2
        col = "D"
        assert self._service.attack_square(row, col, enemies = 2) == ("You missed!", 2)

        row = 1
        col = 3
        self._board.upgrade_board(row, col, "[X]")
        col = "C"
        assert self._service.attack_square(row, col, enemies = 3) == ("Enemy hit!", 3)

        row = 2
        col = 2
        self._board.upgrade_board(row, col, "[*]")
        col = "B"
        assert self._service.attack_square(row, col, enemies = 1) == ("You cannot shoot the stars!", 1)


