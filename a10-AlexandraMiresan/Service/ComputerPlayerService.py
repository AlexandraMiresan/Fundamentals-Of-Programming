import random


class Bot:
    def __init__(self, game_service, repo):
        self.__game_service = game_service
        self.__repo = repo

    def make_a_play(self, turn):
        """
        the computer makes a play, and tries to stop the player from winning when 3 pieces are together
        :param turn:
        :return:
        """
        if turn == 2:
            random_play = random.randint(1, 7)
            self.__game_service.play_piece(random_play, ' ◍ ')
        else:
            row, column = self.check_player_about_to_win(' ◍ ')
            if row == -1 and column == -1:
                row, column = self.check_player_about_to_win(' ◯ ')
                if row == -1 and column == -1:
                    random_play = random.randint(1, 7)
                    self.__game_service.play_piece(random_play, ' ◍ ')
                else:
                    self.__game_service.play_piece(column + 1, ' ◍ ')
            else:
                self.__game_service.play_piece(column + 1, ' ◍ ')
                state = self.__game_service.check_board_state(' ◍ ')
                if state is True:
                    return "Computer wins!"
        return None

    def check_player_about_to_win(self, piece):
        """
        checks if the players is about to win (if there are 3 pieces one next to the other)
        :param piece:
        :return:
        """
        for row in reversed(range(6)):
            for column in reversed(range(7)):
                if self.__repo.board.board[row][column] == piece:
                    win_counter = 0
                    for position in range(4):
                        if row - position >= 0:
                            if win_counter == 3 and self.__repo.board.board[row - position][column] == '\t':
                                    if row - position + 1 <= 5:
                                        if self.__repo.board.board[row - position + 1][column] != '\t':
                                            return row - position, column
                            if self.__repo.board.board[row - position][column] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if row - position >= 0 and column - position >= 0:
                            if win_counter == 3 and self.__repo.board.board[row - position][column - position] == '\t':
                                if row - position + 1 <= 5:
                                    if self.__repo.board.board[row - position + 1][column - position] != '\t':
                                        return row-position , column-position
                            if self.__repo.board.board[row - position][column - position] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if column - position >= 0:
                            if win_counter == 3 and self.__repo.board.board[row][column - position] == '\t':
                                if row + 1 <= 5:
                                    if self.__repo.board.board[row + 1][column - position] != '\t':
                                        return row, column - position
                                elif row == 5:
                                    return row, column - position
                            if self.__repo.board.board[row][column - position] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if row + position <= 5 and column - position >= 0:
                            if win_counter == 3 and self.__repo.board.board[row + position][column - position] == '\t':
                                if row + position + 1 <= 5:
                                    if self.__repo.board.board[row + position + 1][column - position] != '\t':
                                        return row + position, column - position
                                    elif row+position == 5:
                                        return row + position, column - position
                            if self.__repo.board.board[row + position][column - position] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if row + position <= 5 and column + position <= 6:
                            if win_counter == 3 and self.__repo.board.board[row + position][column + position] == '\t':
                                if row + position + 1 <= 5:
                                    if self.__repo.board.board[row + position + 1][column + position] != '\t':
                                        return row + position, column + position
                                elif row+position == 5:
                                    return row + position, column + position
                            if self.__repo.board.board[row + position][column + position] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if column + position <= 6:
                            if win_counter == 3 and self.__repo.board.board[row][column + position] == '\t':
                                if row + 1 <= 5:
                                    if self.__repo.board.board[row + 1][column + position] != '\t':
                                        return row, column + position
                                elif row == 5:
                                    return row, column + position
                            if self.__repo.board.board[row][column + position] == piece:
                                win_counter += 1
                            else:
                                break
                    win_counter = 0
                    for position in range(4):
                        if row - position >= 0 and column + position <= 6:
                            if win_counter == 3 and self.__repo.board.board[row - position][column + position] == '\t':
                                if row - position + 1 <= 5:
                                    if self.__repo.board.board[row - position + 1][column + position] != '\t':
                                        return row - position, column + position
                            if self.__repo.board.board[row - position][column + position] == piece:
                                win_counter += 1
                            else:
                                break
        return -1, -1