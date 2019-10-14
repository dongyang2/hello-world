# coding: utf-8
# Python 3
# 题目太长了


def find_path(li, s):
    ln = len(li)
    if ln <= 0:
        raise ValueError("输入数组需要非空")
    try:
        lm = len(li[0])
        if lm == 0:
            raise ValueError("输入数组需要是二维的")
    except TypeError:
        raise ValueError("输入数组需要是二维的")

    flag = []  # 记录是否走过这里
    for i in range(ln):
        flag.append([False for _ in range(lm)])

    # k = 0
    # for i in range(ln):
    #     for j in range(lm):
    #         if li[i][j] == s[k] and flag[i][j] is False:
    #             li[i][j] = True
    #             stack.append([i, j])
    #             k+=1

    k = 0
    for i in range(ln):
        for j in range(lm):
            if back_track(li, i, j, s, k, flag) is True:
                return True
    del flag
    return False


def back_track(li, row, col, s, si, flag):
    """真正实现回朔函数。row,col表示当前格子，si表示已经匹配到的字符的个数，s是待匹配字符串，flag是那个格子是否已经使用。
     这里其实在思路上做了两个判断。
     一是此格子是否匹配第一个或当前字符。
     二是当前的字符已匹配上了，后面的字符是否可以通过匹配。"""

    # ln = len(li)
    # lm = len(li[0])
    if si == len(s):
        return True

    has_path = False
    if li[row][col] == s[si] and flag[row][col] is False:
        si += 1
        flag[row][col] = True

        # 试探性地向前伸一脚
        has_path = (back_track(li, row, col - 1, s, si, flag) or back_track(li, row - 1, col, s, si, flag) or
                    back_track(li, row, col + 1, s, si, flag) or back_track(li, row + 1, col, s, si, flag))
        # # PEP8: continuation line over-indented for visual indent
        # has_path = back_track(li, row, col - 1, s, si, flag) or back_track(li, row - 1, col, s, si, flag) or \
        #             back_track(li, row, col + 1, s, si, flag) or back_track(li, row + 1, col, s, si, flag)

        # 如果试探失败就撤销这一步
        if has_path is False:
            si -= 1
            flag[row][col] = False

    return has_path


def main():
    # li = [['a', 'b'], ['c', 'd']]
    li = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
    s = 'abfb'
    # s = 'bfce'
    print(find_path(li, s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    # li1 = [2, 3]
    # li1.pop()
    # print(li1)
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
