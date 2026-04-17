from app_logic import process_sensor_data

if __name__ == "__main__":
    print("--- Test 1: Valid Sensor Data ---")
    res1 = process_sensor_data([10.5, 20.0, 15.5])
    print(f"Result 1: {res1}")

    print("--- Test 2: Empty Sensor Data (Will Crash) ---")
    # 模拟传感器故障，传回了空数据，触发崩溃
    res2 = process_sensor_data([])
    print(f"Result 2: {res2}")