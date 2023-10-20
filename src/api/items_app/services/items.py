from ..models.item import Item
from ..database.connection import query_items

def find_all():
    items = query_items()
    return {"items": items}

def find_one(id: int) -> dict[str, Item]:
    try:
        items = query_items()
        item = items[id]
        return {"item": item}
    except:
        raise Exception("Item not found")

def find_by_max_price(price: float):
    items = query_items()
    items = filter(lambda x: x.price <= price, items)
    return {"items": items}
