import unittest

from src.domain.Client import Client
from src.repository.ClientRepository import ClientRepository
from src.repository.RepoException import RepoException


class TestClientRepository(unittest.TestCase):
    def setUp(self):
        """Set up a new ClientRepository for each test."""
        self.repo = ClientRepository()
        self.client1 = Client(1, "Alice")
        self.client2 = Client(2, "Bob")
        self.client3 = Client(3, "Charlie")

    def test_add_client(self):
        """Test adding a client to the repository."""
        self.repo.add_client(self.client1)
        self.assertEqual(len(self.repo.get_all_clients()), 1)
        self.assertEqual(self.repo.get_all_clients()[0].name, "Alice")


        with self.assertRaises(RepoException):
            self.repo.add_client(self.client1)

    def test_get_all_clients(self):
        """Test retrieving all clients from the repository."""
        self.repo.add_client(self.client1)
        self.repo.add_client(self.client2)
        clients = self.repo.get_all_clients()
        self.assertEqual(len(clients), 2)
        self.assertIn(self.client1, clients)
        self.assertIn(self.client2, clients)

    def test_get_client_by_id(self):
        """Test retrieving a client by its ID."""
        self.repo.add_client(self.client1)
        client = self.repo.get_client_by_id(1)
        self.assertEqual(client.name, "Alice")


        self.assertIsNone(self.repo.get_client_by_id(99))

    def test_delete_client(self):
        """Test deleting a client by its ID."""
        self.repo.add_client(self.client1)
        self.repo.add_client(self.client2)
        self.repo.delete_client(1)
        self.assertEqual(len(self.repo.get_all_clients()), 1)
        self.assertNotIn(self.client1, self.repo.get_all_clients())


        self.repo.delete_client(99)
        self.assertEqual(len(self.repo.get_all_clients()), 1)

    def test_update_client(self):
        """Test updating a client's details."""
        self.repo.add_client(self.client1)
        updated_client = Client(1, "Alice Smith")
        self.repo.update_client(updated_client)
        client = self.repo.get_client_by_id(1)
        self.assertEqual(client.name, "Alice Smith")

