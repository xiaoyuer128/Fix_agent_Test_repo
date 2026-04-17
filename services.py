def calculate_cart_total(cart_items: list, user):
    """
    计算购物车总价。
    如果是 VIP 用户，则享受专属折扣。
    """
    base_total = sum(item.price for item in cart_items)

    # 💣 致命 Bug 在这里：如果上游传入的 user 是 None，这里直接取属性会引发 AttributeError
    if user.is_vip:
        final_total = base_total * user.discount_rate
    else:
        final_total = base_total

    return final_total

def process_payment(user_id, amount):
    print(f"Processing payment of {amount} for user {user_id}")
    return True