import os


def each_file_or_dir_name(path):
    """ 遍历指定目录，显示目录下的所有文件或目录名

    :param path: 文件夹的绝对路径或者相对路径
    :return: 该文件夹下的所有文件或文件夹名字的列表
    """
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        # print(child.decode('gbk'))  # .decode('gbk')是解决中文显示乱码问题
        # print(di_or_fi)
        di_fi.append(each_path)
    return di_fi
