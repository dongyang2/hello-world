# 一些可能比较实用的基本操作

from .file_op import read_file, mkdir, is_rectangle, is_rectangle_byte, divide_file, write_file, write_file_li, \
    read_file_li, ergodic_dir, write_csv, move_file, add_suffix_for_dir, get_picture, ergodic_all_file
from .num_op import get_first_ratio, li_precision_control, get_min_2d_list, get_size_top_n_li, get_li_size, slice_li, \
    get_min_li, get_shi, flatten_li, unique, merge_core, gen_random_order
from .text_op import add_blank_after_comma, get_last_dir_name, get_dir, del_str_by_2char, split_num_from_str, \
    add_in_same_dir, get_suffix, get_name

__all__ = ['file_op',
           'date_op',
           'num_op',
           # 'read_pdf',
           'text_op',

           # file_op
           'add_suffix_for_dir',  # 为一个文件夹内所有文件添加统一后缀名
           'divide_file',         # 分割一部分文件作为测试集，一部分作为验证集
           'ergodic_all_file',    # 想象一个树结构，以path为根节点，文件为叶子结点，返回所有叶子结点的路径
           'ergodic_dir',         # 遍历指定目录（新）r_full=True返回全路径，r_full=False仅返回文件和目录名
           'get_picture',         # 复制一个源文件夹下的所有子文件夹中的指定后缀文件，到目标文件夹，且保留源文件夹下子文件夹的结构
           'mkdir',               # 创建目录
           'move_file',           # 移动文件到目录
           'is_rectangle',        # 判断一个文件内容每一行长度是不是一样
           'is_rectangle_byte',   # 对一个二进制文件，判断其内容每一行长度是不是一样
           'read_file',           # 按行读取文件内容且返回一个二维数组
           'read_file_li',        # 读取文件内容，返回一个二维数组，可以指定文件第一行是否有标题，可以指定分隔符
           'write_file',          # 把一维或二维数组写入文件，需要指定w_type，'1D list'和'2D list'二选一
           'write_file_li',       # 把任意维度的数组写入文件
           'write_csv',           # 将类数组的变量保存成csv格式的文件

           # num_op
           'flatten_li',            # 把多维列表各元素放入一个一维列表
           'gen_random_order',      # 获得一个随机的顺序，比如gen_random_order(10)就得到随机的十个数，互补重复，且在[0,9]区间内
           'get_first_ratio',       # 获得一个一维列表前(只看位置不看大小)几成（百分之几十）的所有元素
           'get_li_size',           # 返回列表中各元素的长度
           'get_min_2d_list',       # 获得二维列表中最小元素的值和下标
           'get_min_li',            # 获得一维列表中最小元素的值和下标
           'get_size_top_n_li',     # 获得二维数组长度最大的n个一维数组，n必须被指定
           'get_shi',               # 算一个整数所在的十位段，比如255在250段，136在130段
           'li_precision_control',  # 精度控制，将多维列表中所有元素都进行统一的精度控制
           'slice_li',              # 按比例切分序列
           'unique',                # 一维列表内元素去重

           # text_op
           'add_blank_after_comma',  # 在逗号后面加空格
           'add_in_same_dir',        # 返回一个和给定路径在同一个目录（文件夹）中的路径
           'del_str_by_2char',       # 删除一个字符串中被2个子字符串包围的所有字符
           'get_dir',                # 获得文件的整个目录，即剔除了文件自己的名字
           'get_last_dir_name',      # 从一个文件列表中获得最深层的目录名，目前最大只能支持二维数组
           'get_name',               # 输入是路径，返回名字和后缀
           'get_suffix'              # 获得一个文件的后缀名
           'split_num_from_str',     # 返回字符串中的数字与只包含字母的子字符串
           ]
