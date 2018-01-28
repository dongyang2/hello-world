# operations about file
# -*- coding: UTF-8 -*-

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


def read_file(filename):
    """读取文件内容"""
    f_open = open(filename, 'r')
    file_content = []
    for eachLine in f_open:
        # print("读取到得内容如下：",eachLine)
        row1 = eachLine.split(',')      # 用逗号分割
        # print(row1[-1][:-2])
        row1[-1] = row1[-1][:-1]        # 把回车符去掉，不然写不进数据库
        # print(len(row1))
        file_content.append(row1)
    f_open.close()
    return file_content


def is_rectangle(file_path):
    """判断一个文件内容每一行长度是不是一样"""
    with open(file_path, 'r') as f_c:
        file_content = []
        for each_line in f_c:
            row1 = each_line.split(',')
            row1[-1] = row1[-1][:-1]
            file_content.append(len(row1))
        j = 1
        bool_rectangle = 0
        # print(len(file_content))
        while j < len(file_content):
            if file_content[j] != file_content[j-1]:
                bool_rectangle = 1
                print('The line ', str(j), '(', str(file_content[j]),
                      ') is not equal to the above(', str(file_content[j-1]),  ').')
            j += 1
        if bool_rectangle == 0:
            print('Is rectangle.')


# def see_json(filename):
#     with open(filename, 'r')as f:
#         arr_new = []
#         for i in f:     # i是str类型
#             # print(i, type(i))
#             # print(i.find('{'))
#             j = 1           # 这里是1因为for循环是从第一个开始的，细想下就理解了
#             for k in i:
#                 if k == '{':
#                     i = i[:j] + '\n' + i[j::]
#                 j += 1
#             arr_new.append(i)
#         return arr_new


def write_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in content:
            f.write(i)


if __name__ == '__main__':
    path1 = "../resource/op-cleaver"
    each_name = each_file_or_dir_name(path1)
    for l in each_name:
        print(read_file(l))
        # write_file(see_json(l), l[:-4] + 'txt')
        break

