class Board:
    def __init__(self):
        self.__board = [['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t'],
                        ['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t'],
                        ['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t']]

    @property
    def board(self):
        return self.__board

    def Clear_board(self):
        self.__board = [['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t'],
                        ['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t'],
                        ['\t', '\t', '\t', '\t', '\t', '\t', '\t'], ['\t', '\t', '\t', '\t', '\t', '\t', '\t']]