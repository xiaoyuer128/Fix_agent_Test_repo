def process_order_items(items):
    """处理订单中的多个商品并计算均价"""
    if not items:  # 如果 items 为空，则直接返回 0.0
        return 0.0
    total_price = sum(item['price'] for item in items)
    # 确保 items 非空后再计算平均值
    average_price = total_price / len(items)
    return average_price