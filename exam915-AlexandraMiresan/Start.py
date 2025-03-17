from domain.Board import Board
from tests.Tests import Tests
from ui.UI import UI


def main():
    ui = UI(Board())
    ui.start_ui()

if __name__ == '__main__':
    main()
    test = Tests()