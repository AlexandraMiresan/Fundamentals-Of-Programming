import pickle

from src.repository.ClientRepository import ClientRepository
from src.repository.IOException import IOException


class PickleClientRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            file = open(file_name, "rb")
            self._client_list = pickle.load(file)
            file.close()

        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def add_client(self, client_to_add):
        super().add_client(client_to_add)
        self.__save_file()

    def __save_file(self):
        try:
            file = open(self._file_name, "wb")
            pickle.dump(self._client_list, file)
            file.close()
        except FileNotFoundError:
            raise IOException("File not found")
        except EOFError:
            pass

    def delete_client(self, client_id):
        super().delete_client(client_id)
        self.__save_file()

    def update_client(self, client_to_update):
        super().update_client(client_to_update)
        self.__save_file()

