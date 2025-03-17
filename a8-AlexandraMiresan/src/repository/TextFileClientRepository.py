from src.domain.Client import Client
from src.repository.ClientRepository import ClientRepository
from src.repository.IOException import IOException


class TextFileClientRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self.__load_file(file_name)

    def __load_file(self, file_name):
        try:
            fin = open(file_name, "rt")
            line = fin.readline()
            while len(line) > 0:
                tokens = line.split("|")
                super().add_client(Client(int(tokens[0]), tokens[1].strip()))
                line = fin.readline()
            fin.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def add_client(self, client_to_add):
        super().add_client(client_to_add)
        self.__save_file()

    def __save_file(self):
        try:
            fout = open(self._file_name, "wt")
            for client in self.get_all_clients():
                fout.write(str(client.client_id) + "|" + str(client.name) +"\n")
            fout.close()
        except FileNotFoundError:
            raise IOException("File not found")

    def delete_client(self, client_id):
        super().delete_client(client_id)
        self.__save_file()

    def update_client(self, client_to_update):
        super().update_client(client_to_update)
        self.__save_file()
