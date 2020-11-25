import os
import re
from typing import Dict

from tools import script_tool, shared_tool


def check_invar(aigs_dir: str = "../../resource/aigs") -> Dict[str, Dict[str, bool]]:
    """
    对某个目录下的所有aig格式的网表文件，验证其模型中的所有不变性性质
    :param aigs_dir: 要验证的网表文件的根目录（可以有嵌套子目录）
    :return: 网表文件 -> {不变性公式 -> 验证是否通过}
    """
    res = dict()
    # 当前主目录，当前主目录下的所有目录，当前主目录下的所有文件
    for maindir, subdir, filename_list in os.walk(aigs_dir):
        # 遍历当前主目录下的所有文件
        for filename in filename_list:
            # 检查一下是aig文件
            if filename.endswith(".aig"):
                # 合并成一个完整路径aig文件名
                fullname = os.path.join(maindir, filename)
                res[fullname] = dict()
                # 例化成nuXmv命令脚本
                command_file = script_tool.instantiate("aig_check_invar", {"file_name": fullname})
                # 调用nuXmv进行验证，获得验证结果
                command = "nuXmv -source {}".format(command_file)
                ans = shared_tool.exec_commmand(command)
                # 正则匹配不变性那些行，这里采用多行模式
                pattern = re.compile(r"^-- invariant .* is .*$", flags=re.M)
                inv_anses = pattern.findall(ans)
                # 取出不变性公式和验证结果，加到结果中
                for inv_ans in inv_anses:
                    inv_formula = inv_ans.strip("-- invariant ").strip(" is false").strip(" is true")
                    inv_result = False if inv_ans.split(" is ")[-1] == 'false' else True
                    res[fullname][inv_formula] = inv_result
    return res


if __name__ == '__main__':
    check_ans = check_invar()
    for filename, inv in check_ans.items():
        print(filename)
        for formula, result in inv.items():
            print(formula, " = ", result)
        print()
