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


if __name__ == '__main__':
    unittest.main()
