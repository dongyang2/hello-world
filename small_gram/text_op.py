from small_gram import file_op


def add_blank_after_comma(txt):
    s = ''
    for i, j in enumerate(txt):
        if j != '\n':
            s += j
        if j == ',' and i != ' ':
            s += ' '
    print(s)


def get_last_dir_name(li, dn=-1):
    """从一个文件列表中获得最深层的目录名，目前最大只能支持二维数组
    dn = 1  说明数组元素中最后一个斜杠后面是目录名
    dn = -1 表示数组元素中最后一个斜杠后面是文件名
    """
    dir_li = []
    for i in li:
        if isinstance(i, str):
            if dn == 1:
                s = i.split('/')[-1]
            else:
                s = i.split('/')[-2]
            dir_li.append(s)
            # print(s)
        else:
            for j in i:  # 这里准备写递归的，但是如果是每次加入一个数组，就格式不对齐了，要想只加入元素，返回一个一维数组，只能先写递归展开数组的函数
                if dn == 1:
                    s = j.split('/')[-1]
                else:
                    s = j.split('/')[-2]
                dir_li.append(s)
    return dir_li


def get_dir(fil_nam):
    """获得文件的整个目录"""
    s = fil_nam.split('/')[:-1]
    tmp_s = ''
    for i in s:
        tmp_s += i + '/'
    return tmp_s


def dir_op(dr):
    # 我觉得有时间应该写一个专门处理各种目录名的函数
    pass


if __name__ == '__main__':
    str1 = '''[10930,10318,10595,10972,7706,6756,9092,10551,9722,10913,11151,8186,6422, 
6337,11649,11652,10310,12043,7937,6476,9662,9570,9981,9331,9449,6773,6304,9355, 
10477,10148,10395,11261,8713,7299,10424,10795,11069,11602,11427,9095,7707,10767, 
12136,12812,12006,12528,10329,7818,11719,11683,12603,11495,13670,11337,10232, 
13261,13230,15535,16837,19598,14823,11622,19391,18177,19994,14723,15694,13248, 
9543,12872,13101,15053,12619,13749,10228,9725,14729,12518,14564,15085,14722, 
11999,9390,13481,14795,15845,15271,14686,11054,10395]'''
    # add_blank_after_comma(str1)
    li1 = [['../dataset/丰水梨/20170308103252.jpg',
            '../dataset/丰水梨/20170308103301.jpg',
            '../dataset/丰水梨/20170308103306.jpg'],
           ['../dataset/海南香蕉/Snapshot000104.jpg',
            '../dataset/海南香蕉/Snapshot000105.jpg',
            '../lesson/image_process/dataset/海南香蕉/Snapshot000106.jpg']]
    li2 = ['../丰水梨/Snapshot000104.jpg',
           '../dataset/海南香蕉/Snapshot000105.jpg',
           '../lesson/image_process/dataset/海南香蕉/Snapshot000106.jpg']
    fil1 = 'H:/lesson/image_process/dataset'
    fil_li = file_op.each_file_or_dir_name(fil1)
    # print(fil_li)
    names = get_last_dir_name(fil_li, dn=1)
    print(names)
