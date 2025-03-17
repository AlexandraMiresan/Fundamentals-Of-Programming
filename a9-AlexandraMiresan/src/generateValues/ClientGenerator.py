from faker import Faker

from src.domain.Client import Client


class ClientGenerator:
    def __init__(self):
        self.__faker = Faker()

    def generate_valid_client(self) -> Client:
        id = self.__faker.unique.random_number(digits = 4)
        name = self.__faker.name()
        client = Client(id, name)
        return client


