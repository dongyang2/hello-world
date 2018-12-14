# 一些可能比较实用的基本操作

from .file_op import read_file, mkdir, is_rectangle, is_rectangle_byte, divide_file, write_file, write_file_li, \
    read_file_li, ergodic_dir, write_csv, move_file, add_suffix_for_dir
from .num_op import get_first_ratio, li_precision_control, get_min_2d_list, get_size_top_n_li, get_li_size, slice_li, \
    get_min_li, get_shi, flatten_li, unique, merge_core
from .text_op import add_blank_after_comma, get_last_dir_name, get_dir, del_str_by_2char, split_num_from_str, \
    add_in_same_dir

__all__ = ['file_op',
           'date_op',
           'num_op',
           'read_pdf',
           'text_op',

           # file_op
           'read_file',             # 按行读取文件内容且返回一个二维数组
           'mkdir',                 # 创建目录
           'is_rectangle',          # 判断一个文件内容每一行长度是不是一样
           'is_rectangle_byte',     # 对一个二进制文件，判断其内容每一行长度是不是一样
           'divide_file',           # 分割一部分文件作为测试集，一部分作为验证集
           'write_file',            # 把一维或二维数组写入文件，需要指定w_type，'1D list'和'2D list'二选一
           'write_file_li',         # 把任意维度的数组写入文件
           'read_file_li',          # 读取文件内容，返回一个二维数组，可以指定文件第一行是否有标题，可以指定分隔符
           'ergodic_dir',           # 遍历指定目录（新）
           'write_csv',             # 将类数组的变量保存成csv格式的文件
           'move_file',             # 移动文件到目录
           'add_suffix_for_dir',    # 为一个文件夹内所有文件添加统一后缀名

           # num_op
           'get_first_ratio',       # 获得一个一维列表前(只看位置不看大小)几成（百分之几十）的所有元素
           'li_precision_control',  # 精度控制，将多维列表中所有元素都进行统一的精度控制
           'get_min_2d_list',       # 获得二维列表中最小元素的值和下标
           'get_size_top_n_li',     # 获得二维数组长度最大的n个一维数组，n必须被指定
           'get_li_size',           # 返回列表中各元素的长度
           'slice_li',              # 按比例切分序列
           'get_min_li',            # 获得一维列表中最小元素的值和下标
           'get_shi',               # 算一个整数所在的十位段，比如255在250段，136在130段
           'flatten_li',            # 把多维列表各元素放入一个一维列表
           'unique',                # 一维列表内元素去重

           # text_op
           'add_blank_after_comma',  # 在逗号后面加空格
           'get_last_dir_name',     # 从一个文件列表中获得最深层的目录名，目前最大只能支持二维数组
           'get_dir',               # 获得文件的整个目录，即剔除了文件自己的名字
           'del_str_by_2char',      # 删除一个字符串中被2个子字符串包围的所有字符
           'split_num_from_str',    # 返回字符串中的数字与只包含字母的子字符串
           'add_in_same_dir'        # 返回一个和给定路径在同一个目录（文件夹）中的路径
           ]
