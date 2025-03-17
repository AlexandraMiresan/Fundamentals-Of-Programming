from src.domain.Client import Client
from src.generateValues.ClientGenerator import ClientGenerator
from src.repository.ClientRepository import ClientRepository

from src.repository.PickleClientRepository import PickleClientRepository
from src.repository.PickleRentalRepository import PickleRentalRepository
from src.repository.RentalRepository import RentalRepository

from src.repository.TextFileClientRepository import TextFileClientRepository
from src.repository.TextFileRentalRepository import TextFileRentalRepository


class ClientService:
    def __init__(self, client_repo, rental_repo):
        self._client_repository = client_repo
        self._rental_repository = rental_repo

    def get_repo(self):
        return self._client_repository

    def set_repo(self, repo):
        self._client_repository = repo

    def add_client(self, client):
        self._client_repository.add_client(client)

    def get_all_clients(self):
        return self._client_repository.get_all_clients()

    def search_clients_by_id(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for client in self.get_all_clients():
            if client.client_id == user_input:
                new_list.append(client)
            elif user_input in str(client.client_id):
                new_list.append(client)
        return new_list

    def search_clients_by_name(self, user_input):
        user_input = user_input.strip().lower()
        new_list = []
        for client in self.get_all_clients():
            if client.name == user_input:
                new_list.append(client)
            elif user_input in client.name:
                new_list.append(client)
        return new_list

    def get_by_id(self, client_id):
        for client in self.get_all_clients():
            if client.client_id == client_id:
                return client

    def update_client(self, client):
        self._client_repository.update_client(client)

    def delete_client(self, client_id):
        self._client_repository.delete_client(client_id)
        for rental in self._rental_repository.get_all_rentals():
            if rental.client_id == client_id:
                self._rental_repository.delete_rental(rental.client_id)
