from src.test.TestBookService import TestBookService
from src.test.TestInMemoryRepo import TestInMemoryRepo
from src.test.TestPickle import TestPickleBookRepository
from src.test.TestTextFile import TestTextFileBookRepository
from src.ui.UI import UI


def main():
    print(f"1.In memory\n2.Textfile\n3.Pickle binary")
    choice_of_repo = input("Please input repo type: ")
    match int(choice_of_repo):
        case 1:
            ui = UI("IN_MEMORY")
        case 2:
            ui = UI("TEXTFILE")
        case 3:
            ui = UI("PICKLE")
        case default:
            ui = UI("IN_MEMORY")
    ui.start_ui()


def test():
    testInMemoryRepo = TestInMemoryRepo()
    testPickleRepo = TestPickleBookRepository()
    testFileRepo = TestTextFileBookRepository()
    testBookService = TestBookService()


if __name__ == '__main__':
    test()
    main()
