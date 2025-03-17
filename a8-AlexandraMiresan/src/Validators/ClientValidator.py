from src.Validators import ValidatorException

from src.domain.Client import Client


class ClientValidator:
    @staticmethod
    def validate(client):
        if not isinstance(client, Client):
            raise TypeError("Client must be of type 'Client'")
        if not isinstance(client.client_id, int):
            raise TypeError("Client id must be of type 'int'")
        if len(str(client.client_id)) == 0:
            raise ValidatorException.ValidatorError("Client id is invalid")
        if len(client.name) == 0:
            raise ValidatorException.ValidatorError("Client name is invalid")