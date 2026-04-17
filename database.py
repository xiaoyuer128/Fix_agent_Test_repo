from models import User, Product

# 模拟数据库数据
USERS_DB = {
    "U001": User("U001", "Alice", is_vip=True, discount_rate=0.8),
    "U002": User("U002", "Bob", is_vip=False, discount_rate=1.0)
}

PRODUCTS_DB = {
    "P001": Product("P001", "Laptop", 1000.0),
    "P002": Product("P002", "Mouse", 50.0)
}

def get_user(user_id: str):
    """从数据库获取用户，如果没找到（比如游客），会返回 None"""
    return USERS_DB.get(user_id)

def get_product(prod_id: str):
    return PRODUCTS_DB.get(prod_id)