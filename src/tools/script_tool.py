import os
from typing import Dict

template_dir = "../../resource/template"
instance_dir = "../../resource/instance"


def instantiate(file_name: str, inst_dict: Dict[str, str]) -> str:
    """
    将resource/template/目录下的脚本模板例化到resource/instance/目录下
    :param file_name: 脚本模板名（从resource/template/下开始的名称）
    :param inst_dict: 例化字典，字段->值
    :return: 生成的脚本文件路径
    """
    # 脚本模板的完整相对路径文件名
    source_file = os.path.join(template_dir, file_name)
    # 要例化到的真实文件的完整相对路径文件名
    dest_file = os.path.join(instance_dir, file_name)
    # 覆盖写模式打开要例化到的文件
    with open(dest_file, 'w') as dest_f:
        # 读模式打开模板文件
        with open(source_file, 'r') as source_f:
            # 读取模板文件所有内容
            content = source_f.read()
            # 正则匹配替换
            for key, val in inst_dict.items():
                content = content.replace("${}$".format(key), val)
            # 写入到例化文件中
            dest_f.write(content)
    return dest_file


def test_instantiate():
    """
    单元测试 instantiate
    :return:
    """
    template_file_name = "aig_check_invar"
    full_instance_file_name = os.path.join(instance_dir, template_file_name)
    assert instantiate(template_file_name, {"file_name": "LauZyHou"}) == full_instance_file_name
    assert instantiate(template_file_name, {"file_name": ""}) == full_instance_file_name
    assert instantiate(template_file_name, {"file_name": "\n"}) == full_instance_file_name


if __name__ == '__main__':
    test_instantiate()
