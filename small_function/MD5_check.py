# coding: utf-8
import hashlib
import os


def md5hex(word):
    """ MD5加密算法，返回32位小写16进制符号  """
    if isinstance(word, str):
        word = word.encode("utf-8")
    elif not isinstance(word, str):
        word = str(word)
    m = hashlib.md5()
    m.update(word)
    return m.hexdigest()


def read_chunks(fh):
    fh.seek(0)
    chunk = fh.read(8096)
    while chunk:
        yield chunk
        chunk = fh.read(8096)
    else:  # 最后要将游标放回文件开头
        fh.seek(0)


def md5sum(f_name):
    """ 计算文件的MD5值，将文件分割为 每8k放入内存，而不是将文件一次性放入内存"""

    m = hashlib.md5()
    if isinstance(f_name, str) and os.path.exists(f_name):
        with open(f_name, "rb") as fh:
            for chunk in read_chunks(fh):
                m.update(chunk)
    # 上传的文件缓存 或 已打开的文件流
    elif f_name.__class__.__name__ in ["StringIO", "StringO"] or os.path.isfile(f_name):
        for chunk in read_chunks(f_name):
            m.update(chunk)
    else:
        return ""
    return m.hexdigest()


def ergodic_dir(path):
    """遍历指定目录，返回目录下的所有文件名"""
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        if os.path.isfile(each_path):
            di_fi.append(each_path)
    return di_fi


def get_each_file_md5(path, show_file=True):
    """
    :param path:        目录（文件夹）地址
    :param show_file:   是否显示MD5重复的文件
    """
    li_fi = ergodic_dir(path)
    li_md5 = []
    for i in li_fi:
        # print(i)
        li_md5.append(md5sum(i))
    li_md5_repeat = []
    if show_file is True:
        for ii, i in enumerate(li_md5):
            for j in li_md5[ii+1:]:
                if i == j:
                    if j not in li_md5_repeat:  # 一个md5值只存一次
                        li_md5_repeat.append(j)  # 把md5值有重复情况的md5值存入一个数组
        for md5 in li_md5_repeat:
            repeat_md5_index = [x for x, j in enumerate(li_md5) if j == md5]  # 获得所有md5重复的下标
            for k in repeat_md5_index:
                print(li_fi[k])
            print()

    return li_md5


if __name__ == "__main__":
    # print(md5sum('E:/常用文档/日志/181029.txt'))
    # print(md5sum('E:/常用文档/日志/181030.txt'))
    # print(md5sum('E:/常用文档/日志/20181024.txt'))
    # print(md5sum('E:/常用文档/日志/20181022.txt'))
    get_each_file_md5('E:/常用文档/日志/')
