import os

MDB_CONNECTION = os.getenv("MDB_CONNECTION", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "enemy_soldiers")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "soldier_details")
