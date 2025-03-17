from src.Validators.ClientValidator import ClientValidator
from src.domain.Client import Client
from src.repository.RepoException import RepoException


class ClientRepository:
    def __init__(self):
        self._client_list = []

    def get_all_clients(self):
        """returns a list of all clients"""
        return self._client_list

    def add_client(self, client_to_add):
        """adds a client to the repository"""
        for client in self._client_list:
            if client.client_id == client_to_add.client_id:
                raise RepoException("Client id already exists")

        self._client_list.append(client_to_add)

    def delete_client(self, client_id):
        """deletes a client from the repository"""
        for client in self._client_list:
            if client.client_id == client_id:
                self._client_list.remove(client)

    def update_client(self, client_to_update):
        """updates a client in the repository"""
        for client in self._client_list:
            if client.client_id == client_to_update.client_id:
                client.set_name(client_to_update.name)

    def get_client_by_id(self, client_id) -> Client:
        for client in self._client_list:
            if client.client_id == client_id:
                return client
