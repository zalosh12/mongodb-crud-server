from fastapi import FastAPI, HTTPException
from soldier_service import SoldierService
from models import Soldier,SoldierUpdate


app = FastAPI()
service = SoldierService()


@app.get("/soldiers/")
def get_soldiers():
    soldiers = service.get_all_soldiers()
    return soldiers

@app.get("/soldiers/{soldier_id}")
def get_soldier_by_id(soldier_id: str):
    soldier = service.get_soldier_by_id(soldier_id)
    return soldier

@app.post("/soldiers/")
def create_soldier(soldier: Soldier):
    return service.add_soldier(soldier)

@app.patch("/soldiers/{soldier_id}")
def update_soldier(soldier_id: str, updates: SoldierUpdate):
    updates_dict = updates.dict(exclude_unset=True)
    return service.update_soldier(soldier_id, updates_dict)

@app.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id: str):
    result = service.delete_soldier(soldier_id)

