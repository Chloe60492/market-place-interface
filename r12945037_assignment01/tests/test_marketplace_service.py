import unittest
from marketplace_service import MarketplaceService
from repository import MarketplaceRepository


class TestMarketplaceService(unittest.TestCase):
    def setUp(self):
        """ Setup the test environment. """
        self.repo = MarketplaceRepository(db_name=":memory:")  # Use an in-memory database for tests
        self.service = MarketplaceService(self.repo)

    def test_register_user(self):
        """ Test registering a new user. """
        result = self.service.register_user("user1")
        self.assertEqual(result, "Success")  # Check if user was successfully registered

    def test_register_existing_user(self):
        """ Test registering an already existing user. """
        self.service.register_user("user1")
        result = self.service.register_user("user1")  # Try registering the same user again
        self.assertEqual(result, "Error - user already existing")  # Should return an error message

    def test_create_listing(self):
        """ Test creating a listing for a registered user. """
        self.service.register_user("user1")
        result = self.service.create_listing("user1", "Phone", "Brand new phone", 1000, "Electronics")
        self.assertTrue(result.isnumeric())  # The result should be the ID of the created listing (numeric)

    def test_create_listing_for_nonexistent_user(self):
        """ Test creating a listing for a user that does not exist. """
        result = self.service.create_listing("user2", "Laptop", "New laptop", 1500, "Electronics")
        self.assertEqual(result, "Error - unknown user")  # Should return error as the user doesn't exist

    def test_get_listing(self):
        """ Test getting a listing. """
        self.service.register_user("user1")
        listing_id = int(self.service.create_listing("user1", "Phone", "Brand new phone", 1000, "Electronics"))
        result = self.service.get_listing("user1", listing_id)
        self.assertIn("Phone", result)  # Check if the title is in the result

    def test_get_nonexistent_listing(self):
        """ Test getting a listing that doesn't exist. """
        result = self.service.get_listing("user1", 9999)
        self.assertEqual(result, "Error - not found")  # Should return error as the listing doesn't exist

    def test_get_category(self):
        """ Test getting listings by category. """
        self.service.register_user("user1")
        self.service.create_listing("user1", "Phone", "Brand new phone", 1000, "Electronics")
        result = self.service.get_category("user1", "Electronics")
        self.assertIn("Phone", result)  # Check if the listing title appears in the result

    def test_get_top_category(self):
        """ Test getting the top category with the most listings. """
        self.service.register_user("user1")
        self.service.create_listing("user1", "Phone", "Brand new phone", 1000, "Electronics")
        self.service.create_listing("user1", "Laptop", "Gaming laptop", 1500, "Electronics")
        result = self.service.get_top_category("user1")
        self.assertEqual(result, "Electronics")  # The category with the most listings should be returned


if __name__ == '__main__':
    unittest.main()
