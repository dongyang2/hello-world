# operations about file
# -*- coding: UTF-8 -*-
# each_file_or_dir_name 遍历指定目录，显示目录下的所有文件或目录名
# read_file_influx_db   读取文件内容，为influxDB导入时读数据定制
# read_file             按行读取文件内容且返回一个二维数组
# is_rectangle          判断一个文件内容每一行长度是不是一样
# is_rectangle_byte     对一个二进制文件，判断其内容每一行长度是不是一样
# divide_file           分割一部分文件作为测试集，一部分作为验证集
# read_acc_file         读取acc文件
# mov_file_to_dir_acc       把acc文件移动到一个目录
# write_file            把一维或二维数组写入文件
# write_file_li         把任意维度的数组写入文件
# read_file_li          返回文件内容为一个数组
# write_file_pic_old    把图片的RGB像素点写到文件中
# read_pix_old          把每个RGB像素都读成一个9位的数字
# save_pic              将数据存为图片，ar是numpy.uint8数组
# ergodic_dir           遍历指定目录（新）
# ergodic_and_regular   遍历指定目录且更改烦人的影视作品文件名
# mkdir                 创建目录

import os
import shutil

from PIL import Image

from small_gram import num_op, text_op
from small_gram.text_op import tc


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
    """判断一个文件内容每一行长度是不是一样"""
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
    """分割一部分文件作为测试集，一部分作为验证集"""
    li_lab_file = read_acc_file(label_file)
    for h, i in enumerate(li_lab_file):
        li_lab_file[h] = num_op.get_first_ratio(i, validate_ratio)
    write_file(li_lab_file, 'H:/infosec/validate_list.txt', '2D list')
    efo = each_file_or_dir_name(path_from)
    ct = 0
    for i in li_lab_file:
        for j in i:
            # print(each_c[1:-1])
            # elem = each_c[1:-1]
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


def mov_file_to_dir_acc(path_from, acc_file):
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
            # print(num, type(num))
            # print(num.find('{'))
            j = 1           # 这里是1因为for循环是从第一个开始的，细想下就理解了
            for k in i:
                if k == '{':
                    i = i[:j] + '\n' + i[j::]
                j += 1
            arr_new.append(i)
        return arr_new


def write_file(content, filename, w_type):
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = text_op.get_dir(filename)
        os.makedirs(f)
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


def write_file_li(li, filename, title=''):
    """写一个数组到文件中

    :param li       要写入的数组
    :type li        list
    :param filename 写入的文件名
    :type filename  str
    :param title    标题，会写入文件第一行
    :type title     str
    """
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = text_op.get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    if title != '':
        f.write(title + '\n')
    if type(li[0]) is not list:
        for ii, i in enumerate(li):
            if ii == len(li)-1:
                f.write(str(i))
            else:
                f.write(str(i) + ',')
        f.write('\n')
    else:
        for i in li:
            for jj, j in enumerate(i):
                if jj == len(i)-1:
                    f.write(str(j))
                else:
                    f.write(str(j) + ',')
            f.write('\n')
    f.close()


def read_file_li(filename, have_title=0, split=' '):
    """读取文件内容，每一行存入一个数组，返回一个二维数组，可以指定文件第一行是否有标题，可以指定分隔符"""
    if have_title != 0 and have_title != 1:
        return False
    with open(filename, 'r') as f_open:
        file_content = []
        for k, each_line in enumerate(f_open):
            if k == 0 and have_title == 1:
                # print(each_line)
                file_content.append(each_line[:-1])
            else:
                word = []
                for i in each_line.split(split)[:-1]:
                    word.append(i)
                file_content.append(word)
        return file_content


def write_file_pic_old(li, filename):
    """把图片的RGB像素点写到文件中"""
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = text_op.get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    for i in li:
        for jj, j in enumerate(i):
            if jj != len(i)-1:
                for k in j:
                    f.write(str(k) + ' ')
                f.write(',')
            else:
                f.write(j)
        f.write('\n')
    f.close()


def read_pix_old(file):
    """把每个RGB像素都读成一个9位的数字"""
    f = read_file(file)
    fil_li = []
    for i in f:
        s = i.split(',')
        tmp_li = []
        for jj, j in enumerate(s):
            if jj != len(s)-1:
                si = j.split(' ')
                ss = ''
                for k in si:
                    if len(k) == 1:
                        tmp_s = '00' + k
                    elif len(k) == 2:
                        tmp_s = '0' + k
                    else:
                        tmp_s = k
                    ss = ss + tmp_s
                tmp_li.append(int(ss))
            else:
                tmp_li.append(j)
            # print(each_c)
        fil_li.append(tmp_li)
    return fil_li


def save_pic(ar, fil):
    """将数据存为图片，ar是numpy.uint8数组"""
    im_gr = Image.fromarray(ar)
    try:
        im_gr.save(fil)
    except FileNotFoundError:
        f = text_op.get_dir(fil)
        os.makedirs(f)
        im_gr.save(fil)


def ergodic_dir(path, r_full=True):
    """遍历指定目录，返回目录下的所有文件或目录名
    相对于each_file_or_dir_name，改进有二，一函数名短了，二处理了path
    r_full=True返回全路径，比如C:/abc/d.txt
    r_full=False仅返回文件和目录名，比如d.txt
    """
    s = path[-1]
    if s == '/':
        path = path[:-1]
    # print(path)
    path_dir = os.listdir(path)
    if not r_full:
        return path_dir
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        # print(each_path)
        di_fi.append(each_path)
    return di_fi


def ergodic_and_regular(path):
    """遍历指定目录且更改烦人的影视作品文件名"""
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    for di_or_fi in path_dir:
        # each_path = os.path.join('%s/%s' % (path, di_or_fi))
        new_name = text_op.regular_fil_nam(di_or_fi)
        os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


def mkdir(path):
    """创建目录"""
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    is_exists = os.path.exists(path)

    if not is_exists:
        os.makedirs(path)
        # print (path+' 创建成功')
    else:
        print(tc['yellow']+path+' 目录已存在')  # 如果目录存在则不创建，并提示目录已存在
        return False


def write_csv(w_path, arr):
    """将类数组的变量成csv格式的文件"""
    with open(w_path, 'w', encoding='utf-8')as f:
        for i in arr:
            s = ','.join(i)
            f.write(s+'\n')


def move_file(from_path, to_dir_path):
    """移动文件

    :param from_path: 要移动的文件，这个参数必须指向文件
    :param to_dir_path:   文件移动到的位置，必须是文件夹
    """
    if not os.path.isfile(from_path):
        print("%s not exist!" % from_path)
    else:
        if not os.path.exists(to_dir_path):
            os.makedirs(to_dir_path)  # 创建路径
        shutil.move(from_path, to_dir_path)  # 移动文件
        # print("move %s -> %s" % (from_path, to_path))


def add_suffix_for_dir(path, suffix='.jpg'):
    """为一个文件夹内所有文件添加统一后缀名

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


def get_picture(path, to_dir, sf='jpg'):
    """复制一个源文件夹下的所有子文件夹中的指定后缀文件，到目标文件夹，且保留源文件夹下子文件夹的结构

    :param path:   指定的源文件夹
    :param to_dir: 目标文件夹
    :param sf:     想要复制的文件的后缀名，也可以不是图片
    """
    li_dir_name = ergodic_dir(path)
    for dir_ in li_dir_name:
        li_fi = ergodic_dir(dir_)
        folder = dir_.split('/')[-1]
        to_dir_path = to_dir+'/'+folder
        if not os.path.exists(to_dir_path):
            os.makedirs(to_dir_path)
        for fi in li_fi:
            if text_op.get_suffix(fi) == sf:
                shutil.copy(fi, to_dir_path)


def ergodic_all_file(path):
    """想象一个树结构，以path为根节点，文件为叶子结点，返回所有叶子结点的路径"""
    li_tmp = []
    li_fi = []
    for i in ergodic_dir(path):
        if os.path.isdir(i):
            li_tmp += ergodic_all_file(i)
        else:
            li_fi.append(i)

    return li_tmp+li_fi


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

    # mov_file_to_dir_acc(path3, path5)
    # shutil.move('H:/infosec/trainLabels.csv', 'H:/infosec/test')
    # mov_file_to_dir_acc(path4, path5)

    write_name = 'H:/lesson/image_process/result/features.txt'
    # fea1 = read_pix_old(write_name)
    # for i1 in fea1:
    #     print(i1)

    # for i2 in ergodic_all_file('../interview_q'):
    #     print(i2)

    path6 = 'G:/project_loc/rubbishbin/aabb'
    mkdir(path6)
