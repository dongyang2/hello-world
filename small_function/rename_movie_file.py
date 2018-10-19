# python3.6
# utf-8
# author: github.com/dongyang2
import os


def each_file_or_dir_name(path):
    """ 遍历指定目录，显示目录下的所有文件或目录名
    """
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        print(each_path)
        di_fi.append(each_path)
    return di_fi


def ergodic_dir(path):
    """遍历指定目录，显示目录下的所有文件或目录名
    相对于each_file_or_dir_name，一名字短了，二处理了path
    """
    s = path[-1]
    if s == '/':
        path = path[:-1]
    # print(path)
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        print(di_or_fi)
        di_fi.append(each_path)
    return di_fi


def del_char(s, c):
    """删除字符串中指定字符"""
    s_new = ''
    for i in s:
        if i != c:
            s_new += i
    return s_new


def regular_fil_nam(fil_nam, ds):
    """把影视作品的文件名规范化"""
    remove_website = del_str_by_2char(fil_nam, 'www', 'com')
    remove_website = del_str_by_2char(remove_website, 'www', 'cc')
    remove_website = del_str_by_2char(remove_website, 'www', 'Cc')
    remove_website = del_str_by_2char(remove_website, 'www', 'tv')
    remove_website = del_str_by_2char(remove_website, 'www', 'net')
    remove_website = del_str_by_2char(remove_website, 'www', '转载')
    li_fil = remove_website.split('.')
    nam = ' '.join(li_fil[:-1])
    suffix = li_fil[-1]
    # print(suffix, '|||', nam)
    remove_captions_group = del_str_by_2char(nam, '-', '字幕组')  # 去除字幕组
    remove_cap_gro2 = del_str_by_2char(remove_captions_group, '[', '字幕组')
    nam_final = remove_cap_gro2
    for i in ds:
        # print(i)
        nam_final = nam_final.replace(i, '')
        # print(remove_website)

    if nam_final:
        if nam_final[0] == ' ':  # 去除开头的空格
            nam_final = nam_final[1:]
        if nam_final[-1] == ' ':  # 去除结尾的空格
            nam_final = nam_final[:-1]
        if nam_final[0] == '-':  # 去除开头的短杠
            nam_final = nam_final[1:]
        return nam_final+'.'+suffix
    
    else:  # 这里考虑到了没有文件后缀的情况
        return suffix


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
        # print('No such substring in this string!')
        return s


def ergodic_and_regular(path, ds):
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    for di_or_fi in path_dir:
        # each_path = os.path.join('%s/%s' % (path, di_or_fi))
        new_name = regular_fil_nam(di_or_fi, ds)
        os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


if __name__ == '__main__':
    path1 = 'H:/hello world resource/zhangxuan_resource'
    path2 = 'D:/下载/'

    s_set = ['韩版中英双字幕', '中英双字幕',
             '修正特效中英双字',
             'BD国语中字1280高清', 'BD国语中字', 'HD国语中字',
             'BD中英双字',
             '国语中字', '韩语中字', 'BD中字', 'bd中字',
             '中英双字', '国英双语',
             '国英双语双字',
             '国粤双语',
             '1280X720', '1280x720', '720p', '720P','1080p',
             '1080P',
             '1920x1080', '1920X1080',
             '1280高清', '1024高清',  '1280超清',
             'KO_CN', 'TSKS', 'x264-PublicHD', 'PRiME',
             '[', ']', '(', ')', '【', '】',
             'x264-WiKi', 'x264-HDS',
             'HDTVrip', 'HDTV', 'x264', 'X264', 'BluRay',
             'AAC', 'DTS',
             '无水印', '特效',
             'lol电影天堂', '阳光电影', '66影视', '迅播影院',
             '电影天堂', '迅雷下载', '最新电影', '6v电影',
             '2Audio', '2audio',
             'BD', 'HD', '中字', '  ']  # 这里两个空格最好放在最后面

    ergodic_and_regular(os.getcwd(), s_set)
