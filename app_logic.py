def process_sensor_data(data_list: list):
    """
    处理传感器传入的数据列表，计算平均值。
    """
    # 💣 简单的致命 Bug：没有检查列表是否为空。
    # 当上游传入空列表 [] 时，len(data_list) 为 0，触发 ZeroDivisionError
    average = sum(data_list) / len(data_list)

    # 模拟进一步处理
    result = average * 1.5
    return result


def check_system_health():
    """模拟系统健康检查"""
    return True