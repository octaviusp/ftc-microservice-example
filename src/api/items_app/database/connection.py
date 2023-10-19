from ..models.item import Item

items = [
    Item(name="test", price=10.99, description="test description"),
    Item(name="test2", price=20.99, description="test2 description"),
    Item(name="test3", price=30.99, description="test3 description"),
]

def query_items():
    return items

def connect():
    return True