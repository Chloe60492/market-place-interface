import sqlite3
from datetime import datetime

class MarketplaceRepository:
    def __init__(self, db_name="marketplace.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                username TEXT PRIMARY KEY COLLATE NOCASE)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS listings (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                description TEXT,
                                price INT,
                                category TEXT,
                                username TEXT,
                                created_at TEXT,
                                FOREIGN KEY (username) REFERENCES users(username))''')
        self.conn.commit()

    def user_exists(self, username: str) -> bool:
        self.cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone() is not None

    def add_user(self, username: str) -> str:
        if self.user_exists(username):
            return "Error - user already existing"
        self.cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        self.conn.commit()
        return "Success"

    def add_listing(self, username: str, title: str, description: str, price: int, category: str) -> str:
        if not self.user_exists(username):
            return "Error - unknown user"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO listings (title, description, price, category, username, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                            (title, description, price, category, username, created_at))
        self.conn.commit()
        return str(self.cursor.lastrowid + 100000)

    def get_listing(self, username: str, listing_id: int) -> str:
        if not self.user_exists(username):
            return "Error - unknown user"
        self.cursor.execute("SELECT title, description, price, created_at, category, username FROM listings WHERE id = ?", (listing_id,))
        result = self.cursor.fetchone()
        return "|".join(map(str, result)) if result else "Error - not found"

    def delete_listing(self, username: str, listing_id: int) -> str:
        self.cursor.execute("SELECT username FROM listings WHERE id = ?", (listing_id,))
        result = self.cursor.fetchone()
        if not result:
            return "Error - listing does not exist"
        if result[0].lower() != username.lower():
            return "Error - listing owner mismatch"
        self.cursor.execute("DELETE FROM listings WHERE id = ?", (listing_id,))
        self.conn.commit()
        return "Success"

    def get_listings_by_category(self, username: str, category: str) -> str:
        if not self.user_exists(username):
            return "Error - unknown user"
        self.cursor.execute("SELECT title, description, price, created_at, category, username FROM listings WHERE category = ? ORDER BY created_at DESC", (category,))
        results = self.cursor.fetchall()
        return "\n".join("|".join(map(str, row)) for row in results) if results else "Error - category not found"

    def get_top_category(self, username: str) -> str:
        if not self.user_exists(username):
            return "Error - unknown user"
        self.cursor.execute("SELECT category, COUNT(*) FROM listings GROUP BY category ORDER BY COUNT(*) DESC LIMIT 1")
        result = self.cursor.fetchone()
        return result[0] if result else "Error - unknown user"
