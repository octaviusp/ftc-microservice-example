from pydantic import BaseModel

class Item(BaseModel):
    name: str
    # optional description
    description: str | None = None
    price: float