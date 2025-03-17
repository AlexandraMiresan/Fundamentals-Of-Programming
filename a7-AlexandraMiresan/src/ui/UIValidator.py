from src.ui.UIException import UIException


class UIValidator:
    @staticmethod
    def validate_input(choice: str):
        if not choice.isnumeric():
            raise UIException("Input must be an integer.")

