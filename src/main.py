from fastapi import FastAPI
from .api.items_app.controllers.items import items_router

app = FastAPI()

# adding items routing
app.include_router(items_router, prefix="/api/v1/items")

# more routings examples

"""
from api.controllers.users import users_router
app.include_router(users_router, prefix="/api/v1/users")
"""
