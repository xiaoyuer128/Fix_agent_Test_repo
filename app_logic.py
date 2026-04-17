def process_sensor_data(data_list: list):
    """
    处理传感器传入的数据列表，计算平均值。
    """
    # ✅ 修复：增加对空列表的安全检查
    if not data_list:
        return 0.0  # 或根据业务需求返回 None、抛出异常等

    average = sum(data_list) / len(data_list)

    # 模拟进一步处理
    result = average * 1.5
    return result


def check_system_health():
    """模拟系统健康检查"""
    return True