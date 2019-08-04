from small_gram.custom_error import FunctionValueError


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
    """获得文件的整个目录，即剔除了文件自己的名字"""
    s = fil_nam.split('/')[:-1]
    tmp_s = ''
    for i in s:
        tmp_s += i + '/'
    return tmp_s


def del_str_by_2char(s, co, ct, f=True):
    """删除一个字符串中被2个子字符串包围的所有字符
    f=True删除指定的那两个子字符串
    f=False不删除指定的那两个子字符串
    """
    if co in s and ct in s:
        ind_one = s.find(co)
        ind_two = s.find(ct)
        if f is True:
            ind_end = ind_two+len(ct)
            ca = s[ind_one: ind_end]
            # print(ca)
            return s.replace(ca, '')
        else:
            ind_start = ind_one+len(co)
            ca = s[ind_start: ind_two]
            return s.replace(ca, '')
    else:
        print('\033[33;0m'+'No such substring in this string!')
        return s


def regular_fil_nam(fil_nam):
    """把影视作品的文件名规范化，最新的版本详见small_function/rename_movie_file.py"""
    ds = ['1280X720', '1280x720', '720p', '720P', 'KO_CN', 'TSKS',
          '1080p', '1920x1080', '1920X1080', '1080P', '[', ']',
          '(', ')', 'HDTVrip', '阳光电影', 'HDTV', 'x264', 'X264'
          'AAC', '国语中字', 'HD', '中字', '  ']

    remove_website = del_str_by_2char(fil_nam, 'www', 'com')
    li_fil = remove_website.split('.')
    nam = ' '.join(li_fil[:-1])
    suffix = li_fil[-1]
    remove_captions_group = del_str_by_2char(nam, '-', '字幕组')
    nam_final = remove_captions_group
    for i in ds:
        # print(num)
        nam_final = nam_final.replace(i, '')
        # print(remove_website)

    if nam_final:
        if nam_final[0] == ' ':
            nam_final = nam_final[1:]
        if nam_final[-1] == ' ':
            nam_final = nam_final[:-1]
        return nam_final+'.'+suffix
    else:  # 这里考虑到了没有文件后缀的情况
        return suffix


def split_num_from_str(s):
    """ 把数字从字符串中删除
    :return: 返回字符串中的数字与只包含字母的子字符串
    """
    import re
    # return re.findall(r'([0-9][0-9]+)([a-z]+)', s)
    int_num = r'(\-\d+|\+\d+|\d+)'
    word = r'[a-zA-Z]+'
    return re.findall(int_num, s), re.findall(word, s)


def add_in_same_dir(di_fi, add, slash='/'):
    """返回一个和di_fi在一个目录中的路径
    :param di_fi: 文件路径或者文件夹路径
    :param add:   指定的文件名
    :param slash: 正斜杠"/"或者反斜杠"\"
    :return 一个文件名叫add的，与di_fi在同一个文件夹下的路径
    """
    error_color = FunctionValueError.error_color['red']
    if slash != '/' and slash != '\\':
        # print('\033[31m%s is Invalid slash!\33[0m' % slash)
        # return False
        raise FunctionValueError('%s%s is Invalid slash!\33[0m' % (error_color, slash))
    if add[0] == '\\':
        # print('''\033[31mPlease use '/' but not '\\' to prevent bad things from happening!\33[0m''')
        # return False
        raise FunctionValueError(''''%sPlease use '/' but not %s to prevent bad things from happening!''' %
                                 (error_color, add[0]))
    if add[0] == '/':
        add = add[1:]

    if di_fi[-1] == '/' or di_fi[-1] == '\\':
        return di_fi+add

    s_li = di_fi.replace('\\', '/').split('/')[:-1]
    return slash.join(s_li+[add])


def get_suffix(fi):
    """获得一个文件的后缀名"""
    return fi.split('/')[-1].split('.')[-1]


# # txt color
# tc = {
#     'red': '\033[31;0m',
#     'green': '\033[32;0m',
#     'yellow': '\033[33;0m',
#     'blue': '\033[34;0m'
# }


def get_name(s):
    """s是路径，返回名字和后缀"""
    whole_name = s.split('/')[-1]
    f_name, suffix = whole_name.split('.')
    return f_name, suffix


def del_the_elem(content, li):
    """删除content中所有出现在li中的元素，li若是单个字符，请以列表的形式指定。
    比如要删除content中所有的j，则li指定为['j']。"""
    lc = len(content)-1  # 指针从最后一个元素开始往前跑
    while lc != 0:
        if content[lc] in li:
            content = content[:lc]+content[lc+1:]
        lc -= 1
    return content


def zz_match(s, pat):
    """利用re包来进行正则匹配，返回匹配的字符串"""
    import re
    search_result = re.search(pat, s)
    if search_result is not None:
        index1, index2 = search_result.span()
        return s[index1:index2]
    else:
        raise FunctionValueError('No Match! Please retry your string or pattern.')


def get_match_index(s, pat):
    """找到所有符合pat的字符串的下标

    比如，s='abcdefg', pat=r'd'
    返回[(3,4)]
    """
    import re
    li = []
    index_li = re.finditer(pat, s)
    for i in index_li:
        li.append(i.span())
    return li


def str_reverse(s: str):
    """翻转字符串"""
    if len(s) == 0:
        raise ValueError('请输入非空字符串')
    tmp_s = ''
    for s_i in s[::-1]:
        tmp_s += s_i
    return tmp_s


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
#     from small_gram import file_op
    # fil_li = file_op.each_file_or_dir_name(fil1)
    # print(fil_li)
    # names = get_last_dir_name(fil_li, dn=1)
    # print(names)

    str2 = '235436niaohonafn-4363agbag'
    # print(split_num_from_str(str2))

    dir2 = 'H:\DF_emotion\\xy\\'
    # print(add_in_same_dir(dir2, '\\ok', '/'))

    # print(get_suffix(li2[0]))

    # print(tc['yellow'] + 'aaa')

    li_xxx = ['\xa0', '\xa1', '\xa2', '\xa3', '\xa4', '\xa5', '\xa6', '\xa7',
              '\xa8', '\xa9', '\xaa', '\xab', '\xac', '\xad', '\xae', '\xaf',
              '\ufffd', '\u2022']
    # for i3 in li_xxx:
    #     print(i3)

    zz_match(str1, r'333')
