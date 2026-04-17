class User:
    def __init__(self, user_id, name, is_vip=False, discount_rate=1.0):
        self.user_id = user_id
        self.name = name
        self.is_vip = is_vip
        self.discount_rate = discount_rate

class Product:
    def __init__(self, prod_id, name, price):
        self.prod_id = prod_id
        self.name = name
        self.price = price