from pydantic import BaseModel
from datetime import datetime


class TicketData(BaseModel):
    from_cityFrom: str
    from_cityCodeFrom: str
    from_local_departure: datetime

    to_cityFrom: str
    to_cityCodeFrom: str
    to_local_departure: datetime

    nightsInDest: int
    price: int
