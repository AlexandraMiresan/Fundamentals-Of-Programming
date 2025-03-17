import unittest
from unittest.mock import MagicMock

from src.domain.Client import Client
from src.domain.Rental import Rental
from src.services.ClientService import ClientService

class TestClientService(unittest.TestCase):
    def setUp(self):
        """Set up mock repositories and service for each test."""
        self.mock_client_repo = MagicMock()
        self.mock_rental_repo = MagicMock()
        self.service = ClientService(self.mock_client_repo, self.mock_rental_repo)

        self.client1 = Client(1, "Alice")
        self.client2 = Client(2, "Bob")
        self.client3 = Client(3, "Charlie")

        self.rental1 = Rental(1, 1, 101, "2024-01-01")
        self.rental2 = Rental(2, 2, 102, "2024-01-05")

    def test_add_client(self):
        """Test adding a client through the service."""
        self.service.add_client(self.client1)
        self.mock_client_repo.add_client.assert_called_once_with(self.client1)

    def test_get_all_clients(self):
        """Test retrieving all clients through the service."""
        self.mock_client_repo.get_all_clients.return_value = [self.client1, self.client2]
        clients = self.service.get_all_clients()
        self.assertEqual(len(clients), 2)
        self.assertIn(self.client1, clients)
        self.assertIn(self.client2, clients)

    def test_search_clients_by_id(self):
        """Test searching for clients by ID."""
        self.mock_client_repo.get_all_clients.return_value = [self.client1, self.client2]
        result = self.service.search_clients_by_id("1")
        self.assertEqual(len(result), 1)
        self.assertIn(self.client1, result)

    def test_search_clients_by_name(self):
        """Test searching for clients by name."""
        self.mock_client_repo.get_all_clients.return_value = [self.client1, self.client2, self.client3]
        result = self.service.search_clients_by_name("Bob")
        self.assertEqual(len(result), 1)
        self.assertIn(self.client2, result)

    def test_get_by_id(self):
        """Test retrieving a client by ID."""
        self.mock_client_repo.get_all_clients.return_value = [self.client1, self.client2]
        client = self.service.get_by_id(1)
        self.assertEqual(client, self.client1)

    def test_update_client(self):
        """Test updating a client through the service."""
        updated_client = Client(1, "Alice Smith")
        self.service.update_client(updated_client)
        self.mock_client_repo.update_client.assert_called_once_with(updated_client)

    def test_delete_client(self):
        """Test deleting a client through the service."""
        self.mock_rental_repo.get_all_rentals.return_value = [self.rental1, self.rental2]
        self.service.delete_client(1)
        self.mock_client_repo.delete_client.assert_called_once_with(1)
        self.mock_rental_repo.delete_rental.assert_called_once_with(1)

