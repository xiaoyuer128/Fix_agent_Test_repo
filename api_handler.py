from .utils import get_user, get_product
from .services import calculate_cart_total
from .payment import process_payment

class CheckoutAPI:
    def handle_checkout(self, request_payload: dict):
        """处理前端传来的结算请求"""
        user_id = request_payload.get("user_id")
        product_ids = request_payload.get("products", [])

        # 上游源头：这里获取用户，如果是不存在的用户，user 会变成 None
        user = get_user(user_id)

        # 修复点1: 如果用户不存在（guest 或无效用户），应拒绝结算或按非VIP处理
        if user is None:
            # 可选策略：拒绝结算，或视为普通用户（此处选择拒绝）
            return {"status": "failed", "reason": "invalid_user"}

        cart_items = []
        for pid in product_ids:
            prod = get_product(pid)
            if prod:
                cart_items.append(prod)

        # 此时 user 已确保非 None
        total_amount = calculate_cart_total(cart_items, user)

        if process_payment(user_id, total_amount):
            return {"status": "success", "amount_paid": total_amount}
        return {"status": "failed"}