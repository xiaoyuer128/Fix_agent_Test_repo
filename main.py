from api_handler import CheckoutAPI

if __name__ == "__main__":
    api = CheckoutAPI()

    print("--- Test 1: Valid VIP User ---")
    req1 = {"user_id": "U001", "products": ["P001", "P002"]}
    res1 = api.handle_checkout(req1)
    print(f"Result: {res1}\n")

    # 触发崩溃的边缘测试用例：未注册的游客用户
    print("--- Test 2: Invalid/Guest User ---")
    req2 = {"user_id": "U999", "products": ["P001"]} # U999 在数据库里不存在
    # 调用链：api_handler -> 查库返回 None -> 传给 services -> 取 is_vip 时崩溃
    res2 = api.handle_checkout(req2)
    print(f"Result: {res2}\n")