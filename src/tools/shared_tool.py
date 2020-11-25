import os


def exec_commmand(command: str) -> str:
    """
    执行一条命令，返回结果
    :param command: 命令字符串
    :return: 命令执行输出的结果
    """
    tmp = os.popen(command)
    res = tmp.read()
    tmp.close()
    return res
