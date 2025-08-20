from pymongo import MongoClient
import os
import shortuuid

class Dal:
    def __init__(self,MDB_CONNECTION, db_name, collection_name):
        self.con_string = MDB_CONNECTION
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def create_connection(self):
        try:
            self.client = MongoClient(self.con_string)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            print(f"Connected to {self.db_name}.{self.collection_name}")
        except Exception as e:
            print(f"connection error: {e}")

    def get_all(self):
        try:
            docs = list(self.collection.find({},{"_id":0}))
            # for d in docs:
            #     d["_id"] = str(d["_id"])
            return docs
        except Exception as e:
            return {f"error: {e}"}

    def get_one(self,item_id: str):
        result = self.collection.find_one({"id":item_id})
        return result

    def create_item(self, item: dict):
        result = self.collection.insert_one(item)
        # self.collection.
        return {"message": "Item created successfully"}

    def update_item(self, item_id: str, updates: dict):
        result = self.collection.update_one({"id": item_id}, {"$set": updates})
        if result.modified_count > 0:
            return {"message": "Item updated successfully"}
        return {"error": "No item found or no changes applied"}

    def delete_item(self, item_id: str):
        result = self.collection.delete_one({"id": item_id})
        if result.deleted_count > 0:
            return {"message": "Item deleted successfully"}
        return {"error": "No item found"}

    def close_connection(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")
















# from bson import ObjectId
# from pymongo import MongoClient
# import os
#
#
# class Dal:
#     def __init__(self,db_name='enemy_soldiers',collection_name='soldier_details'):
#         self.connection = os.getenv("MDB_CONNECTION","mongodb://localhost:27017/")
#         self.db_name = db_name
#         self.collection_name = collection_name
#         self.client = None
#         self.db = None
#         self.collection = None
#
#     def create_connection(self):
#         self.client = MongoClient(self.connection)
#         self.db = self.client[self.db_name]
#         self.collection = self.db[self.collection_name]
#         print("Successfully connected to the database")
#
#     def get_all(self) :
#         details = list(self.collection.find())
#         for d in details:
#             d["_id"] = str(d["_id"])
#         return details
#
#     def create_item(self,item: dict):
#         result = self.collection.insert_one(item)
#         return {"message" : "Item created successfully", "id" : str(result.inserted_id)}
#
#     def update_item(self, item_id: str, updates: dict):
#         result = self.collection.update_one({"_id":ObjectId(item_id)}, {"$set":updates})
#         if result.modified_count > 0:
#             return {"message" : "Item updated successfully"}
#         return {"error" : "No item found or no changes applied"}
#
#     def delete_item(self, item_id: str) :
#         result = self.collection.delete_one({"_id" : ObjectId(item_id)})
#         if result.deleted_count > 0 :
#             return {"message" : "Item deleted successfully"}
#         return {"error" : "No item found"}
#
#
#     def close_connection(self) :
#         """Close MongoDB connection."""
#         if self.client :
#             self.client.close()
#             print("MongoDB connection closed.")

#
# if __name__ == "__main__":
#     my_dal = Dal()
#     my_dal.create_connection()
#     soldier = {"first":"ahmed","last":"abed"}
#     my_dal.create_item(soldier)
#     print(my_dal.get_all())
#     my_dal.close_connection()

