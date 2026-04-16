def connect_db(host, port):
    print(f"Connecting to database at {host}:{port}...")
    return True

def fetch_user_data(user_id):
    # 模拟从数据库获取数据
    return {"id": user_id, "name": "Test User", "status": "active"}