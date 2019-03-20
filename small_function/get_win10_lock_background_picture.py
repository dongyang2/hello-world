# py3.5
# utf-8
# author: github.com/dongyang2
# 获取选择Windows聚焦的锁屏壁纸（win10）
import os
import shutil
import getpass

from small_gram import add_suffix_for_dir, move_file


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
            # copy_file(inp, to_dir)  # 这里本来是想复制的，但是提示没有权限，就只好移动了
            move_file(file, to_dir)
    # print(li_file_name)


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
