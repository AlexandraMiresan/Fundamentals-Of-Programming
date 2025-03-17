from service.GameOverException import GameOverException
from service.Service import Service


class UI:
    def __init__(self, board):
        self._service = Service(board)

    def start_ui(self):
        try:
            self._service.place_stars()
            self._service.place_enemies()
            enemies = 2
            text = " "
            while enemies > 0:
                self.print_board()
                enemies, text = self.attack(enemies)
                if text == "You missed!":
                    self.move_enemies(enemies)
                    self.check_if_lost()
                self.check_if_won(enemies)
        except GameOverException as ge:
            print(ge)
            return

    def check_if_lost(self):
        self._service.check_if_lost()

    def print_board(self):
        for row in self._service.get_board():
            print(row)

    def attack(self, enemies):
        try:
            row = int(input("Enter the row you want to hit: "))
            col = input("Enter the column you want to hit: ")
            text, enemies = self._service.attack_square(row, col, enemies)
            print(text)
            return enemies, text
        except ValueError as ve:
            print(ve)

    def move_enemies(self, enemies):
        self._service.move_enemies(enemies)

    def check_if_won(self, enemies):
        if enemies == 0:
            raise GameOverException("You won!")



