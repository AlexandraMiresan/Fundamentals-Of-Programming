
from src.services.UndoService import FunctionCall, Operation, CascadedOperation


class ClientService:
    def __init__(self, client_repo, rental_repo, undo_service, rental_service):
        self._client_repository = client_repo
        self._rental_repository = rental_repo
        self._undo_service = undo_service
        self._rental_service = rental_service

    def get_repo(self):
        return self._client_repository

    def set_repo(self, repo):
        self._client_repository = repo

    def add_client(self, client):
        self._client_repository.add_client(client)

        functionRedo = FunctionCall(self._client_repository.add_client, client)
        functionUndo = FunctionCall(self._client_repository.delete_client, client)
        operation = [Operation(functionUndo, functionRedo)]

        self._undo_service.recordUndo(operation)

        return client

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

    def update_client(self, client_to_update):
        client = self._client_repository.get_client_by_id(client_to_update.client_id)

        functionRedo = FunctionCall(self._client_repository.update_client, client_to_update)
        functionUndo = FunctionCall(self._client_repository.update_client, client)
        operation = [Operation(functionUndo, functionRedo)]

        self._undo_service.recordUndo(operation)
        return client_to_update

    def delete_client(self, client_id):
        client = self._client_repository.get_client_by_id(client_id)
        self._client_repository.delete_client(client_id)
        rentalRepo = self._rental_repository.get_all_rentals().copy()
        for rental in self._rental_repository.get_all_rentals():
            if client.client_id == rental.client_id:
                self._rental_repository.delete_rental(rental.rental_id)

        functionRedo = FunctionCall(self._client_repository.delete_client, client_id)
        functionUndo = FunctionCall(self._client_repository.add_client, client)
        operations = [Operation(functionUndo, functionRedo)]

        for rental in rentalRepo:
            if client.client_id == rental.client_id:
                functionRedo = FunctionCall(self._rental_repository.delete_rental, rental.rental_id)
                functionUndo = FunctionCall(self._rental_repository.rent_a_movie, rental)
                operations.append(Operation(functionUndo, functionRedo))

        self._undo_service.recordUndo(CascadedOperation(*operations))

