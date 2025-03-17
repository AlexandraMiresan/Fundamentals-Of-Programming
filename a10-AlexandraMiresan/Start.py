from Domain.board import Board
from Repository.Repository import Repository
from Service.ComputerPlayerService import Bot
from Service.GameService import GameService
from Service.Validator import Validator
from Tests.Tests import GameServiceTest, TestBOTService, TestGameError
from UI.UI import UI


def start():
    board = Board()
    repository = Repository(board)
    validator = Validator()
    service = GameService(repository, validator)
    bot = Bot(service, repository)
    ui = UI(service, bot)
    ui.start_ui()


if __name__ == '__main__':
    start()
    GameServiceTest()
    TestBOTService()
    TestGameError()
