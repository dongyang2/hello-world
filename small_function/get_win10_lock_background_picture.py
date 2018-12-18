# py3.5
# utf-8
# author: github.com/dongyang2
# 获取选择Windows聚焦的锁屏壁纸（win10）
import os
import shutil
import getpass


def each_file_or_dir_name(path):
    """ 遍历指定目录，显示目录下的所有文件

    :param path: 文件夹的绝对路径或者相对路径
    """
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        di_fi.append(each_path)
    return di_fi


def move_file(from_path, to_dir_path):
    """移动文件

    :param from_path: 要移动的文件，这个参数必须指向文件
    :param to_dir_path:   文件移动到的位置，必须是文件夹
    """
    if not os.path.isfile(from_path):
        print("%s not exist!" % from_path)
    else:
        # fil_dir, fil_name = os.path.split(to_dir_path)  # 分离文件名和路径
        if not os.path.exists(to_dir_path):
            os.makedirs(to_dir_path)  # 创建路径
        shutil.move(from_path, to_dir_path)  # 移动文件
        # print("move %s -> %s" % (from_path, to_path))


def copy_file(srcfile, to_dir_path):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        if not os.path.exists(to_dir_path):
            os.makedirs(to_dir_path)
        shutil.copyfile(srcfile, to_dir_path)


def get_picture(to_dir):
    path = 'C:/Users/' + getpass.getuser() + '/AppData/Local/Packages/' \
                                             'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
    li_file_name = each_file_or_dir_name(path)
    for file in li_file_name:
        fi_size = os.path.getsize(file)/float(1024)  # 文件大小
        fi_size_kb = round(fi_size, 2)
        if fi_size_kb > 200:
            # copy_file(file, to_dir)  # 这里本来是想复制的，但是提示没有权限，就只好移动了
            move_file(file, to_dir)
    # print(li_file_name)


def add_suffix_for_dir(path, suffix='.jpg'):
    """为一个文件夹内所有文件添加后缀名

    :param path:   文件夹地址
    :param suffix: 想要加的后缀
    """
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    for fi_name in path_dir:
        new_name = fi_name + suffix
        os.rename('%s/%s' % (path, fi_name), '%s/%s' % (path, new_name))


def main():
    default_path = 'E:/win10锁屏壁纸'
    given_path = input('请输入想要存放的文件夹地址：')
    if given_path != '':
        default_path = given_path
    get_picture(default_path)
    add_suffix_for_dir(default_path)


if __name__ == "__main__":
    file1 = 'E:/下载/rename.txt'
    dir_path1 = 'E:/下载/test/'
    # move_file(file1, dir_path1)

    main()
