import unittest
import sqlite3
import sys

sys.path.append("./src")

from database import DataBase


class TestContactDatabase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase()
        self.connection = sqlite3.connect(
            ":memory:"
        )  # Use in-memory database for testing
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.connection.close()

    def test_create_contact(self):
        self.db.create_contact(
            "John Doe", "1234567890", "john@example.com", "123 Main St"
        )
        contact = self.db.contact_detail(name="John Doe")
        self.assertIsNotNone(contact)
        self.assertEqual(contact[1:], ("1234567890", "john@example.com", "123 Main St"))

    def test_update_contact(self):
        self.db.create_contact(
            "Jane Smith", "9876543210", "jane@example.com", "456 Elm St"
        )
        self.db.update_contact(
            "Jane Smith", "Jane Johnson", "jane@example.com", "9876543210", "456 Elm St"
        )
        updated_contact = self.db.contact_detail(name="Jane Johnson")
        self.assertIsNotNone(updated_contact)
        self.assertEqual(
            updated_contact[1:], ("9876543210", "jane@example.com", "456 Elm St")
        )

    def test_search_contact(self):
        self.db.create_contact("Alice", "1111111111", "alice@example.com", "123 Elm St")
        self.db.create_contact("Bob", "2222222222", "bob@example.com", "456 Oak St")
        self.db.create_contact(
            "Charlie", "3333333333", "charlie@example.com", "789 Pine St"
        )

        # Search by name
        results_by_name = self.db.search("Alice")
        self.assertEqual(len(results_by_name), 1)
        self.assertEqual(results_by_name[0][1], "Alice")

        # Search by partial name
        partial_results_by_name = self.db.search("Char")
        self.assertEqual(len(partial_results_by_name), 1)
        self.assertEqual(partial_results_by_name[0][1], "Charlie")

        # Search by phone number
        results_by_phone = self.db.search(phone_num="2222222222")
        self.assertEqual(len(results_by_phone), 1)
        self.assertEqual(results_by_phone[0][2], "2222222222")

    def test_delete_contact(self):
        self.db.create_contact(
            "Test User", "9999999999", "test@example.com", "789 Maple St"
        )
        self.db.del_contact("Test User")
        deleted_contact = self.db.contact_detail(name="Test User")
        self.assertIsNone(deleted_contact)

    def test_invalid_input_create_contact(self):
        # Test create contact with incomplete data
        with self.assertLogs(level="WARNING"):
            self.db.create_contact("Incomplete Contact", "", "", "")
        # Ensure no contact is created
        contact = self.db.contact_detail(name="Incomplete Contact")
        self.assertIsNone(contact)

    def test_nonexistent_contact_detail(self):
        # Test fetching detail for non-existent contact
        contact = self.db.contact_detail(name="Nonexistent")
        self.assertIsNone(contact)

    def test_update_nonexistent_contact(self):
        # Test updating a non-existent contact
        with self.assertLogs(level="ERROR"):
            self.db.update_contact(
                "Nonexistent",
                "New Name",
                "new@example.com",
                "1234567890",
                "New Address",
            )

    def test_delete_nonexistent_contact(self):
        # Test deleting a non-existent contact
        with self.assertLogs(level="ERROR"):
            self.db.del_contact("Nonexistent")


if __name__ == "__main__":
    unittest.main()
