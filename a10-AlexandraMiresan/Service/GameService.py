from Service.GameException import GameError


class GameService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def __str__(self):
        message = ""
        for lists in self.__repo.board.board:
            message = message + "|"
            for elements in lists:
                message = message + elements + ','
            message = message + "|"
            message = message + "\n"
        return message

    def play_piece(self, column, piece):
        """
        places a piece on the board
        :param column:
        :param piece:
        :return:
        """
        self.__validator.validate_play(column)
        column = int(column) - 1
        row = -1
        for position in reversed(range(6)):
            if self.__repo.board.board[position][column] == '\t':
                row = position
                break
        if row == -1:
            raise GameError(["invalid location"])
        self.__repo.update(column, row, piece)

    def check_board_state(self, piece):
        """
        checks the state of the board (if either of the players are about to win)
        :param piece:
        :return:
        """
        for row in range(6):
            for column in range(7):
                if self.__repo.board.board[row][column] == piece:
                    win = self.check_win(row, column, piece)
                    if win is True:
                        return True
        return False

    def check_win(self, row, column, piece):
        """
        checks if any of the players have won
        :param row:
        :param column:
        :param piece:
        :return:
        """
        win_counter = 0
        for position in range(4):
            if row - position >= 0:
                if self.__repo.board.board[row - position][column] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if row - position >= 0 and column - position >= 0:
                if self.__repo.board.board[row - position][column - position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if column - position >= 0:
                if self.__repo.board.board[row][column - position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if row + position <= 5 and column - position >= 0:
                if self.__repo.board.board[row + position][column - position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if row + position <= 5:
                if self.__repo.board.board[row + position][column] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if row + position <= 5 and column + position <= 6:
                if self.__repo.board.board[row + position][column + position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if column + position <= 6:
                if self.__repo.board.board[row][column + position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        win_counter = 0
        for position in range(4):
            if row - position >= 0 and column + position <= 6:
                if self.__repo.board.board[row - position][column + position] == piece:
                    win_counter += 1
                else:
                    break
        if win_counter == 4:
            return True
        return False


