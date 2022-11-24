# coding: utf-8
# Python 3
#
#


import sys


def check_pswd(s: str, lower_li: list, uper_li: list, num_li: list):
    """实现遍历两遍的版本，也可以只遍历一遍"""
    if len(s) < 9:
        # print("len")
        return False

    ty_li = []
    for ch in s:
        if ch in lower_li:
            ty_li.append(0)
        elif ch in uper_li:
            ty_li.append(1)
        elif ch in num_li:
            ty_li.append(2)
        elif ch != " " and ch != "\n":
            ty_li.append(3)
    ty_set = set(ty_li)
    # print("set ",ty_set)
    if len(ty_set) < 3:
        return False

    for i in range(len(s) - 2):
        tmp = s[i:i + 3]
        # print("tmp ",tmp)
        inds = s.count(tmp)
        # print("inds ",inds)
        if inds > 1:
            return False
    return True


def main():
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    lower_li = [x for x in s1]
    uper_li = [x for x in s1.upper()]
    num_li = [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

    for line in sys.stdin:
        if check_pswd(line.strip(), lower_li, uper_li, num_li):
            print("OK")
        else:
            print("NG")


if __name__ == '__main__':
    main()
