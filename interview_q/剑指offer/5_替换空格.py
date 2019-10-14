# coding: utf-8
# Python 3
# 在二维数组中找一个数，这个二维数组设定是从左到右递增，且从上到下递增。


def replace_space(s: str, r: str):
    """类似剑指offer的思路。
    因为Python里面没有一格一格移动的操作（至少我不晓得），就先统计一下位置然后再加上。假装我们移动了哈。"""
    ls = len(s)
    tmp = []
    for i in range(ls):
        if s[i] == ' ':
            tmp.append(i)
    tmp_s = ''
    j = 0
    for i in range(ls):
        if j < len(tmp):
            if i == tmp[j]:
                tmp_s += r
                j += 1
            else:
                tmp_s += s[i]
        else:
            tmp_s += s[i]
    return tmp_s


def replace_space_python(s, r):
    """上面那个我真的看不下去了，来个正常的。嗯，这很符合Python的形象。"""
    tmp_s = ''
    for i in s:
        tmp_s += r if i == ' ' else i
    return tmp_s


def main():
    s = "We are happy."
    r = '%20'
    print(replace_space_python(s, r))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
