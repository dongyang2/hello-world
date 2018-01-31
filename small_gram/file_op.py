# operations about file
# -*- coding: UTF-8 -*-

import os
from information_security import read_bytes
from small_gram import num_op
import shutil


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


def read_file_influx_db(filename, encode):
    """读取文件内容，为influxDB导入时读数据定制"""
    if encode == 'utf-8':
        f_open = open(filename, 'r', encoding=encode)
    else:
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


def read_file(filename):
    """读取文件内容"""
    with open(filename, 'r', encoding='utf-8') as f_open:
        file_content = []
        for each_line in f_open:
            file_content.append(each_line[:-1])     # 去掉回车符
        return file_content


def is_rectangle(file_path, file_type):
    """判断一个文件内容每一行长度是不是一样
    """
    file_content = []
    if file_type == 'influx':
        f_c = open(file_path, 'r')
        for each_line in f_c:
            row1 = each_line.split(',')
            row1[-1] = row1[-1][:-1]
            file_content.append(len(row1))
        f_c.close()
    elif file_type == 'byte':
        f_c = open(file_path, 'rb')
        for each_line in f_c:
            row1 = str(each_line[2:-2])[2:-1].split(' ')
            file_content.append(len(row1))
        f_c.close()
    j = 1
    bool_rectangle = 0
    # print(len(file_content))
    while j < len(file_content)+1 and bool_rectangle < 20:
        if file_content[j] != file_content[j-1]:
            bool_rectangle += 1
            print('Line ', str(j+1), '(length ', str(file_content[j]),
                  ') is not equal to the above(', str(file_content[j-1]),  ').')
        j += 1
    if bool_rectangle == 0:
        print('Is rectangle.')


def is_rectangle_byte(file_path):
    f_c = open(file_path, 'rb')
    file_content = []
    for each_line in f_c:
        row1 = str(each_line)[2:-1].split(' ')
        file_content.append(len(row1))


def divide_file(path_from, path_to, validate_ratio, label_file):
    li_lab_file = read_acc_file(label_file)
    for h, i in enumerate(li_lab_file):
        li_lab_file[h] = num_op.get_first_ratio(i, validate_ratio)
    write_file(li_lab_file, 'H:/infosec/validate_list.txt', '2D list')
    efo = each_file_or_dir_name(path_from)
    ct = 0
    for i in li_lab_file:
        for j in i:
            # print(j[1:-1])
            # k = j[1:-1]
            str1 = path_from + '/' + j + '.png'
            str2 = path_to + '/'
            if str1 in efo:
                shutil.move(str1, str2)
                ct += 1
            if ct % 100 == 0:
                print('move ', ct, ' files')


def read_acc_file(acc_file):
    fl = read_file_influx_db(acc_file, '')
    num_of_label = 9
    lf = []
    i = 0
    while i < num_of_label:
        li = []
        lf.append(li)
        i += 1
    for h, i in enumerate(fl):
        if h == 0:
            continue
        else:
            lf[int(i[1]) - 1].append(i[0][1:-1])  # lf[0]存入类标为1的样本 lf[1]存类标为2的样本
    return lf


def mov_file_to_dir(path_from, acc_file):
    li_lab_f = read_acc_file(acc_file)
    di_lab_f = {}
    for h, i in enumerate(li_lab_f):
        for j in i:
            di_lab_f[j] = h+1
    # print(di_lab_f)
    path_dir = os.listdir(path_from)
    di_fi = []
    b = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']     # 这一行是为了某格式特定的
    for di_or_fi in path_dir:
        if di_or_fi in b:
            continue
        else:
            each_path = os.path.join('%s/%s' % (path_from, di_or_fi))
            di_fi.append(each_path)
    for i in di_fi:
        str1 = i.split('/')[-1][:-4]
        label = di_lab_f[str1]          # 获得i对应的类标
        str2 = path_from + '/' + str(label)
        shutil.move(i, str2)


def see_json(filename):
    """未完待续"""
    with open(filename, 'r')as f:
        arr_new = []
        for i in f:     # i是str类型
            # print(i, type(i))
            # print(i.find('{'))
            j = 1           # 这里是1因为for循环是从第一个开始的，细想下就理解了
            for k in i:
                if k == '{':
                    i = i[:j] + '\n' + i[j::]
                j += 1
            arr_new.append(i)
        return arr_new


def write_file(content, filename, w_type):
    f = open(filename, 'w', encoding='utf-8')
    if w_type == '1D list':
        for i in content:
            f.write(i)
    elif w_type == '2D list':
        for h, i in enumerate(content):
            for j in i:
                f.write(j + ' ' + str(h+1) + '\n')
            # f.write(' ' + str(h) + '\n')
    f.close()


if __name__ == '__main__':
    # path1 = "../resource"
    # each_name = each_file_or_dir_name(path1)
    # for l in each_name:
    #     # print(read_file(l))
    #     # write_file(see_json(l), l[:-4] + 'txt', '1D list')
    #     m = read_file(l)
    #     for n in m:
    #         # print(n)
    #         break
    #     break

    # path2 = 'H:/infosec/lan'
    # each_name2 = read_bytes.each_byte_file_name_info_sec(path2)
    # for l in each_name2:
    #     print(l)
    #     is_rectangle(l, 'byte')

    path3 = 'H:/infosec/train_image'
    path4 = 'H:/infosec/validate_image'
    path5 = 'H:/infosec/trainLabels.csv'
    # divide_file(path3, path4, 3, path5)       # 用来把单一训练图片分为训练集和测试集的

    # mov_file_to_dir(path3, path5)
    # shutil.move('H:/infosec/trainLabels.csv', 'H:/infosec/test')
    mov_file_to_dir(path4, path5)
