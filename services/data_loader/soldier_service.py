from dal import Dal
from models import Soldier
import config

class SoldierService:
    def __init__(self):
        self.dal = Dal(
            MDB_CONNECTION=config.MDB_CONNECTION,
            db_name=config.DB_NAME,
            collection_name=config.COLLECTION_NAME)
        self.dal.create_connection()

    def add_soldier(self, soldier: Soldier):
        return self.dal.create_item(soldier.dict())

    def get_all_soldiers(self):
        records = self.dal.get_all()
        return [Soldier(**rec) for rec in records]

    def get_soldier_by_id(self,soldier_id: str):
        return self.dal.get_one(soldier_id)


    def update_soldier(self, soldier_id: str, updates: dict):
        return self.dal.update_item(soldier_id, updates)

    def delete_soldier(self, soldier_id: str):
        return self.dal.delete_item(soldier_id)

    def close(self):
        self.dal.close_connection()
