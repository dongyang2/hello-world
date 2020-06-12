# coding: utf-8
# python3.6
# author: github.com/dongyang2
import os


def each_file_or_dir_name(path):
    """ 遍历指定目录，显示目录下的所有文件或目录名"""
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

    # 删除字幕组
    prefix = ['-', '[', '.']
    for i in prefix:
        fil_nam = del_str_by_2char(fil_nam, i, '字幕组')
        fil_nam = del_str_by_2char(fil_nam, i, '影视')

    # 删除网站名字
    fil_nam = del_str_by_2char(fil_nam, 'www', '转载')
    website_suffix = ['com', 'cc', 'co', 'tv', 'net']
    for i in website_suffix:
        tmp_li = [i]
        upper_word('', i, tmp_li)
        for j in tmp_li:
            fil_nam = del_str_by_2char(fil_nam, 'www', j)
        # print('aaa', fil_nam)

    # 20191216 找到的新规律
    for i in ds['来源']:
        tmp_li = [i]
        upper_word('', i, tmp_li)
        for j in tmp_li:
            fil_nam = del_str_by_2char(fil_nam, j, '.', rt=True, f=0)

    # 删除x264
    fil_nam = del_str_by_2char(fil_nam, 'x264', '.')

    # 20200413
    fil_nam = del_str_by_2char(fil_nam, "BluRay", ".")

    li_fil = fil_nam.split('.')
    nam = ' '.join(li_fil[:-1])
    suffix = li_fil[-1]
    # print(suffix, '|||', nam)

    # 按库去除各项元素
    for i in ds['来源']:
        for j in ds['字幕']:
            nam = nam.replace(i+j, '')
    for i in ds['字幕']:
        nam = nam.replace(i, '')
    for i in ds['杂项']:
        nam = nam.replace(i, '')

    nam_final = nam
    if nam_final[0] == ' ':  # 去除开头的空格
        nam_final = nam_final[1:]
    if nam_final[-1] == ' ':  # 去除结尾的空格
        nam_final = nam_final[:-1]
    if nam_final[0] == '-':  # 去除开头的短杠
        nam_final = nam_final[1:]
    return nam_final+'.'+suffix


def del_str_by_2char(s, co, ct, ro=False, rt=False, f=2):
    """删除一个字符串中被2个子字符串包围的所有字符
    f=0     仅删除s中的co
    f=1     仅删除s中的ct
    f=2     删除s中的co和ct
    f=3     不删除co，也不删除ct

    ro      是否从后往前寻找co
    rt      是否从后往前寻找ct
    """
    if co in s and ct in s:
        ind1 = s.find(co)
        if ro is True:
            ind1 = s.rfind(co)
        ind2 = s.find(ct, ind1)
        if rt is True:
            ind2 = s.rfind(ct)
        # print('ind1 = {}, ind2 = {}'.format(ind1, ind2))

        if f == 1:
            ind1 = ind1+len(co)
            ind2 = ind2+len(ct)
        elif f == 2:
            ind2 = ind2+len(ct)
        elif f == 3:
            ind1 = ind1+len(co)
        ca = s[ind1: ind2]
        # print('--ca--', ca)
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
        suffix = di_or_fi.split('.')[-1]
        if is_movie(suffix) is True:
            new_name = regular_fil_nam(di_or_fi, ds)
            os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


def is_caption(s):
    # 根据规律判定是否是字幕说明
    zimu = ['字幕', '双字', '中字', '双语']
    for i in zimu:
        if i in s:
            return True
    return False


def is_movie(s: str):
    # 根据后缀判断是否是电影文件
    movie_suffix = ['mkv', 'mp4', 'rmvb', 'qmv', 'mov', 'flv']
    if s.lower() in movie_suffix:
        return True
    else:
        return False


def upper_word(p, s, li):
    # 遍历所有大写的方式。原来就是二叉树的遍历啊。
    # li.append(p+s)
    s1u = s[0].upper()+s[1:]
    if len(s) > 1:
        li.append(p+s1u)
        upper_word(p+s[0], s[1:], li)
        upper_word(p+s[0].upper(), s[1:], li)
    else:
        li.append(p+s.upper())
    # return s1u


def test():
    sl = ["闪电侠.The.Flash.S06E04.中英字幕.HDTVrip.720P-人人影视.mp4",
          "www.be457y4jehwahw.com.兰开斯特之王.BD.1080p.中英双字幕.mkv",
          "www.srAHNBr3eqh4weyh4.com.闪电侠第六季第03集中英双字.mkv",
          "The.Flash.2014.S06E05.720p.HDTV.x264-SVA[eztv].mkv",
          "脉冲.impulse.s01e01.720p.Classic字幕组.mp4",
          "神奇女侠BD国英双语双字.电影天堂.www.3j5h4j2.com.mkv",
          "www.b3wh4h3.com.攀登者.HD.1080p.国语中英双字.mp4",
          "www.n34h3qh.com.神奇女侠：血脉.BD.1080p.中英双字幕.mkv",
          "www.n34hqhgh.com.狮子王.BD.1080p.国粤英三语双字.mkv",
          "[www.n3qh4h3qh.com转载]社交网络DVD中英双字.rmvb",
          "【6v电影www.n3qygq.com】蜀山传.720p.国粤双语.BD中字.mkv",
          "中转停留.720p.HD中字[最新电影www.nq3h4yq3.tv].mp4",
          "十年日 本www n3qyh3qyh Co.mp4",
          "韦科惨案.Waco.E02.中英字幕.WEB.720p-人人影视.mp4",
          "[小调网-www.xiaodiao.com]雷神奇侠BD中英双字.rmvb"]

    for i in sl:
        new_name = regular_fil_nam(i, dic)
        print(new_name)


def main():
    # path1 = 'H:/hello world resource/zhangxuan_resource'
    # path2 = 'D:/下载/'

    ergodic_and_regular(os.getcwd(), dic)


if __name__ == '__main__':

    dic = {
        '杂项':
        [
            '1280X720', '1280x720', '720p', '720P', '1080p',
            '1080P',
            '1920x1080', '1920X1080',
            '1280高清', '1024高清', '1280超清',
            'KO_CN', 'TSKS', 'x264-PublicHD', 'PRiME',
            '[', ']', '(', ')', '【', '】',
            'x264-WiKi', 'x264-HDS', 'BluRay',
            'HDTVrip', 'HDTV', 'x264', 'X264',
            'AAC', 'DTS',
            '无水印', '特效',
            'lol电影天堂', '阳光电影', '66影视', '迅播影院',
            '电影天堂', '迅雷下载', '最新电影', '6v电影',
            '人人影视', '小调网',
            '2Audio', '2audio', 'eztv',
            'DVD',
            '  '
        ],  # 这里两个空格最好放在最后面
        '字幕':
        [
            '双字幕', '中英', '韩版',
            '双字', '修正特效',
            '中字', '国语', '韩语',
            '三语', '国粤英', '英国粤', '国英粤',
            '双语', '国英', '国粤',
            '字幕',
        ],
        '来源':
        [
            'HD', 'BD', 'WEB',
        ]
    }
    main()
    # test()
