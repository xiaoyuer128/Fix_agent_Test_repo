from database import get_user, get_product
from services import calculate_cart_total, process_payment

class CheckoutAPI:
    def handle_checkout(self, request_payload: dict):
        """处理前端传来的结算请求"""
        user_id = request_payload.get("user_id")
        product_ids = request_payload.get("products", [])

        # 上游源头：这里获取用户，如果是不存在的用户，user 会变成 None
        user = get_user(user_id)

        cart_items = []
        for pid in product_ids:
            prod = get_product(pid)
            if prod:
                cart_items.append(prod)

        # 危险透传：没有检查 user 是否为 None，直接传给了下游的 services 层
        total_amount = calculate_cart_total(cart_items, user)

        if process_payment(user_id, total_amount):
            return {"status": "success", "amount_paid": total_amount}
        return {"status": "failed"}