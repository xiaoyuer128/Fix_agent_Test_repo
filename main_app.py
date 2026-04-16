from utils import process_order_items
from database import connect_db


def handle_request():
    connect_db("localhost", 3306)
    # 假设这里接收到了一个空订单
    empty_order_list = []

    print("正在处理订单...")
    avg = process_order_items(empty_order_list)
    print(f"订单均价为: {avg}")


if __name__ == "__main__":
    handle_request()