from repository import MarketplaceRepository

class MarketplaceService:
    def __init__(self, repository: MarketplaceRepository):
        self.repo = repository

    def register_user(self, username: str):
        return self.repo.add_user(username)

    def create_listing(self, username: str, title: str, description: str, price: int, category: str):
        return self.repo.add_listing(username, title, description, price, category)

    def delete_listing(self, username: str, listing_id: int):
        return self.repo.delete_listing(username, listing_id)

    def get_listing(self, username: str, listing_id: int):
        return self.repo.get_listing(username, listing_id)

    def get_category(self, username: str, category: str):
        return self.repo.get_listings_by_category(username, category)

    def get_top_category(self, username: str):
        return self.repo.get_top_category(username)
