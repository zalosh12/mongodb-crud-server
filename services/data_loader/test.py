










from models import Soldier
from soldier_service import SoldierService

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app:app",   # המודול והאובייקט FastAPI
        host="0.0.0.0",
        port=8511,
        reload=True       # מתאים לפיתוח, לא חובה בטסטים
    )

# if __name__ == "__main__":
#     from soldier_service import SoldierService
#     from models import Soldier
#
#     service = SoldierService()
#
#     s1 = Soldier(
#         id="123456",  # או אפשר להשאיר ריק
#         first_name="Ahmed",
#         last_name="Abed",
#         phone_number="0501234567",
#         rank="Private"
#     )
#
#     res = service.add_soldier(s1)
#
#
#     soldiers = service.get_all_soldiers()
#     print(soldiers)
#
#     service.update_soldier(soldiers[0].id, {"rank" : "Sergeant"})
#
#     service.delete_soldier(soldiers[0].id)
#
#     service.close()
#
#     service = SoldierService()
#
#     s = Soldier(id="0998865",first_name="Ahmed", last_name="Abed", phone_number="0501234567", rank="Private")
#     print(service.add_soldier(s))
#
#
#     print(service.get_all_soldiers())
#
#     soldiers = service.get_all_soldiers()
#     if soldiers:
#         print(service.update_soldier(soldiers[0].id, {"rank": "Sergeant"}))
#
#     if soldiers:
#         print(service.delete_soldier(soldiers[0].id))
#
#     service.close()
