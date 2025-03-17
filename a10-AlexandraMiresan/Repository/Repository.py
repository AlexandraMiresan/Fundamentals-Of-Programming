
class Repository:
    def __init__(self, board):
        self.__board = board

    @property
    def board(self):
        return self.__board

    def update(self, column, row, piece):
        self.__board.board[row][column] = piece


