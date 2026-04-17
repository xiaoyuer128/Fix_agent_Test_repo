def process_sensor_data(data_list: list) -> float:
    """处理传感器传入的数据列表，计算平均值。"""
    # 增加对空列表的安全检查
    if not data_list:
        return 0.0  # 根据业务需求选择返回0.0

    # 检查data_list中的所有元素是否为数值类型
    if not all(isinstance(item, (int, float)) for item in data_list):
        raise ValueError('All elements in data_list must be numeric. Non-numeric values found.')

    # 新增：检查数据列表中的元素之和是否为0
    if sum(data_list) == 0:
        return 0.0  # 如果总和为0，则直接返回0.0避免除以零错误

    average = sum(data_list) / len(data_list)

    # 模拟进一步处理
    result = average * 1.5
    return result

def check_system_health() -> bool:
    """模拟系统健康检查"""
    return True