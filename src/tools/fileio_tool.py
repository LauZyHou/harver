import time


def create_file(abspath: str) -> None:
    """
    在绝对路径指定的位置创建文件
    如果文件已经存在，会清除文件中的内容
    :param abspath: 要创建文件的位置
    :return: None
    """
    try:
        with open(abspath, 'w') as _:
            pass
    except IOError:
        raise


def additional_write_file(abspath: str, content: str) -> None:
    """
    在绝对路径指定的位置追加写入文件
    :param abspath: 要追加写的文件位置
    :param content: 追加写的内容
    :return: None
    """
    try:
        with open(abspath, 'a+') as f:
            f.write(content)
    except IOError:
        raise


def log_with_time(abspath: str, *logs) -> None:
    """
    写入日志，带有时间信息
    :param abspath: 日志文件的绝对路径
    :param logs: 日志的内容，使用变长元组参数
    :return: None
    """
    try:
        with open(abspath, 'a+') as f:
            time_format_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write("[{}]\n".format(time_format_str))
            for log in logs:
                f.write("{}\n".format(log))
            f.write("\n")
    except IOError:
        raise
