from src.repository import BookRepository
from src.services.BookServiceException import BookServiceException


class UndoService:
    def __init__(self):
        self._history = []

    def save_history(self, repository: BookRepository):
        self._history.append(repository)

    def pop_history(self):
        if len(self._history) <= 1:
            raise BookServiceException(["Undo unavailable."])

        return self._history.pop()