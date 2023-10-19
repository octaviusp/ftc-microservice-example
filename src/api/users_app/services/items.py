from ..models.item import Item

items = [
    Item(name="test", price=10.99, description="test description"),
    Item(name="test2", price=20.99, description="test2 description"),
    Item(name="test3", price=30.99, description="test3 description"),
]

def find_all():
    return {"items": items}

def find_one(id: int) -> dict[str, Item] | Exception:
    try:
        item = items[id]
        return {"item": item}
    except:
        return Exception("Item not found")

def find_by_max_price(price: float):
    items = filter(lambda x: x.price <= price, items)
    return {"items": items}
