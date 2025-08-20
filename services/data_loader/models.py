from pydantic import BaseModel
from typing import Optional
import shortuuid

class Soldier(BaseModel):
    id: str
    first_name: str
    last_name: str
    phone_number: str
    rank: str

class SoldierUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    rank: Optional[str] = None