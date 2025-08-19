from pymongo import MongoClient
import os


class Dal:
    def __init__(self,db_name='enemy_soldiers',collection_name='soldier_details'):
        self.connection = os.getenv("MDB_CONNECTION","mongodb://localhost:27017/")
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def create_connection(self):
        self.client = MongoClient(self.connection)
        self.db = self.client['enemy_soldiers']
        self.collection = self.db['soldier_details']
        print("Successfully connected to the database")

    def get_all(self) :
        details = list(self.collection.find())
        for d in details:
            d["_id"] = str(d["_id"])
        return details


    def create_item(self,item):
        result = self.collection.insert_one(item)
        return {"message": "item created successfully"}

    def close_connection(self) :
        """Close MongoDB connection."""
        if self.client :
            self.client.close()
            print("MongoDB connection closed.")


if __name__ == "__main__":
    my_dal = Dal()
    my_dal.create_connection()
    soldier = {"first":"ahmed","last":"abed"}
    my_dal.create_item(soldier)
    print(my_dal.get_all())
    my_dal.close_connection()

