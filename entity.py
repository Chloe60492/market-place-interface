from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    username: str

@dataclass
class Listing:
    listing_id: int
    title: str
    description: str
    price: int
    category: str
    username: str
    created_at: datetime

@dataclass
class Category:
    name: str