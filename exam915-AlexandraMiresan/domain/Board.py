class Board:
    def __init__(self):
        self._board = [["[0]", "[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]"],
                       ["[1]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ["[2]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ["[3]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ["[4]", "[ ]", "[ ]", "[ ]", "[E]", "[ ]", "[ ]", "[ ]"],
                       ["[5]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ["[6]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ["[7]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                       ]

    def board(self):
        return self._board

    def board_row_col(self, row, col):
        return self._board[row][col]

    def upgrade_board(self, row, col, piece):
        self._board[row][col] = piece