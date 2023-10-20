from ..services.items import find_all

"""
THIS MODULE FOCUSES ON SHARE THE ITEMS_APP RESOURCES TO ANOTHER APP
"""

def provide_items():
    return find_all()
