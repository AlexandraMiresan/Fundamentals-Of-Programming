from Service.GameException import GameError


class Validator:

    @staticmethod
    def validate_play(column):
        if str(column).isnumeric() is False:
            raise GameError(["invalid input for a column"])
        if int(column) < 1 or int(column) > 7:
            raise GameError(["invalid location"])