from Service.GameException import GameError


class UI:
    def __init__(self,serv,bota):
        self.__game_service = serv
        self.__turn = 1
        self.__bot = bota

    def printRules(self):
        print("Welcome to Connect Four!")
        print("RULES:")
        print("Be the first player to connect four of your pieces vertically, horizontally, or diagonally.")
        print("-> Players take turns dropping one piece into a column of their choice.")
        print("-> Pieces fall to the lowest available space in the column.")
        print("-> The first player to align four consecutive pieces in any direction wins.")
        print("-> If the grid is filled without any player connecting four, the game is a draw.")
        print()

    def start_ui(self):
        self.printRules()
        while True:
            try:
                    if self.__turn % 2 == 1:
                        print(self.__game_service)
                        user_input = input("Where to play a piece? >")
                        self.__game_service.play_piece(user_input,' ◯ ')
                        state = self.__game_service.check_board_state(' ◯ ')
                        if state is True:
                            print(str(self.__game_service))
                            print("you win!")
                            return
                        self.__turn += 1
                    else:
                        cwin = self.__bot.make_a_play(self.__turn)
                        if cwin is not None:
                            print(str(self.__game_service))
                            print(cwin)
                            return
                        self.__turn +=1
            except GameError as ge:
                print(str(ge))
