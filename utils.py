def calculate_discount(price, discount_rate):
    """计算折扣价格"""
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("折扣率必须在 0 到 1 之间")
    return price * (1 - discount_rate)

def process_order_items(items):
    """处理订单中的多个商品并计算均价"""
    total_price = sum(item['price'] for item in items)
    # 这里藏着一个潜在的除以零 Bug，当 items 为空时会报错
    average_price = total_price / len(items)
    return average_price