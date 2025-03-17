from random import randint, random, shuffle

from service.GameOverException import GameOverException


class Service:
    def __init__(self, board):
        self._board = board

    def place_stars(self):
        number_of_stars = 8
        while number_of_stars > 0:
            row = randint(1, 7)
            col = randint(1,7)
            if self._board.board_row_col(row, col) == "[ ]":
                if self.is_space_available(row, col):
                    self._board.upgrade_board(row, col, "[*]")
                    number_of_stars -= 1


    def is_space_available(self, row, col):
        if col < 7 and self._board.board_row_col(row, col + 1) == "[*]":
            return False
        if col > 1 and self._board.board_row_col(row, col - 1) == "[*]":
            return False
        if row < 7 and self._board.board_row_col(row + 1, col) == "[*]":
            return False
        if row > 1 and self._board.board_row_col(row - 1, col) == "[*]":
            return False
        if row > 1 and col > 1 and self._board.board_row_col(row - 1, col - 1) == "[*]":
            return False
        if row < 7 and col < 7 and self._board.board_row_col(row + 1, col + 1) == "[*]":
            return False
        if row < 7 and col > 1 and self._board.board_row_col(row + 1, col - 1) == "[*]":
            return False
        if row > 1 and col < 7 and self._board.board_row_col(row - 1, col + 1) == "[*]":
            return False
        return True

    def get_board(self):
        return self._board.board()

    def place_enemies(self):
        number_of_enemies = 2
        while number_of_enemies > 0:
            row = randint(1, 7)
            list = [1, 7]
            shuffle(list)
            if row != 1 or row != 7:
                row = list[0]
            col = randint(1, 7)
            if self._board.board_row_col(row, col) == "[ ]":
                if self.is_space_on_the_edge(row, col):
                    self._board.upgrade_board(row, col, "[X]")
                    number_of_enemies -= 1

    def is_space_on_the_edge(self, row, col):
        if self._board.board_row_col(row, col) != "[ ]":
            return False
        return True

    def translate_input(self, col):
        if col == "A":
            col = 1
        if col == "B":
            col = 2
        if col == "C":
            col = 3
        if col == "D":
            col = 4
        if col == "E":
            col = 5
        if col == "F":
            col = 6
        if col == "G":
            col = 7
        return col

    def move_enemies(self, enemies):
        list = ["move closer", "don't move closer"]
        shuffle(list)
        rowi = 0
        coli = 0
        for row in range(1, 8):
            for col in range(1, 8):
                if self._board.board_row_col(row, col) == "[X]" and rowi != row and coli != col:
                    self._board.upgrade_board(row, col, "[ ]")
                    if list[0] == "move closer":
                        if row == 1 or row == 7:
                            col = randint(2, 6)
                            numbers = [2, 6]
                            shuffle(numbers)
                            row = numbers[0]
                            while self._board.board_row_col(row, col) == "[*]":
                                col = randint(2, 6)
                                numbers = [2, 6]
                                shuffle(numbers)
                                row = numbers[0]
                                self._board.upgrade_board(row, col, "[X]")
                                rowi = row
                                coli = col
                        else:
                            col = randint(3, 5)
                            numbers = [3, 5]
                            shuffle(numbers)
                            row = numbers[0]
                            while self._board.board_row_col(row, col) == "[*]":
                                col = randint(3, 5)
                                numbers = [3, 5]
                                shuffle(numbers)
                                row = numbers[0]
                        self._board.upgrade_board(row, col, "[X]")
                        rowi = row
                        coli = col
                    else:
                        row = randint(1, 7)
                        numbers = [1, 7]
                        shuffle(numbers)
                        row = numbers[0]
                        col = randint(1, 7)
                        while self._board.board_row_col(row, col) == "[*]":
                            row = randint(1, 7)
                            numbers = [1, 7]
                            shuffle(numbers)
                            row = numbers[0]
                            col = randint(1, 7)
                        self._board.upgrade_board(row, col, "[X]")
                        rowi = row
                        coli = col





    def attack_square(self, row, col, enemies):
        """
        attacks the specified square and checks if an enemy was hit, a star was hit or an empty square,
        in case an enemy was hit the function will keep count of that and return the number of the enemies along with
        a message
        :param row:
        :param col:
        :param enemies:
        :return:
        """
        col = self.translate_input(col)
        if self.is_enemy_hit(row, col):
            self._board.upgrade_board(row, col, "[-]")
            enemies -= 1
            return "Enemy hit!", enemies
        elif self._board.board_row_col(row, col) == "[ ]":
            self._board.upgrade_board(row, col, "[h]")
            return "You missed!", enemies
        elif self._board.board_row_col(row, col) == "[*]":
            return "You cannot shoot the stars!", enemies


    def is_enemy_hit(self, row, col):
        if self._board.board_row_col(row, col) == "[X]":
            return True

    def check_if_lost(self):
        for row in range(3, 6):
            for col in range(3, 6):
                if self._board.board_row_col(row, col) == "[X]":
                    raise GameOverException("You lost!")













