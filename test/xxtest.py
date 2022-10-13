import os  # 这里的os就是operation system的含义
import sys
from pathlib import Path  # 导入第三方安装包
import argparse
# argparse库是Python自带的一个命令行参数解析库。它可以处理选项参数(optional argument)和位置参数(positional argument)，并能根据参数信息自动生成使用帮助信息

# 创建解析器
parser = argparse.ArgumentParser(
    description='example argument parser')

print(parser)
#ArgumentParser(prog='xxtest.py',
#               usage=None,
#               description='example argument parser',
#               formatter_class=<class 'argparse.HelpFormatter'>,
#               conflict_handler='error',
#               add_help=True)

# # 获取当前运行脚本文件的绝对路径  F:\github\yolov5_2\test\xxtest.py
# FILE = Path(__file__).resolve()
#
# # 获取当前运行脚本文件所在文件夹路径  F:\github\yolov5_2\test
# ROOT = FILE.parents[0]
#
# print(FILE)
# print(ROOT)
#
#
# # 将上述文件路径转换为绝对路径
# if str(ROOT) not in sys.path:   # 判断路径是否在查询路径列表中
#     sys.path.append(str(ROOT))  # add ROOT to PATH
# ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative 绝对路径转化为相对路径
#
# print(ROOT)  #相对路径输出
# print(ROOT/'test')   # 相对路径下text文件路径


# # 获取当前运行文件所在的文件夹路径（当前的工作文件夹路径）
# print(os.getcwd())#与.等价
# print(os.path.abspath('.'))
# # 获取当前运行文件路径
# print(os.path.abspath('xxtest.py'))
# # 获取当前文件所在文件夹的上级目录
# print(os.path.abspath('..'))
