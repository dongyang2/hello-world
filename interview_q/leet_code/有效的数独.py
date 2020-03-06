# https://leetcode-cn.com/problems/valid-sudoku/
# coding: utf-8
# Python 3
# 给定一个9*9的数组，判断是否属于有效的数独，且只需要检查行、列、九宫格是否合法，不需判断是否有解。
# 思路：
# 边界条件：


def basic_check(li: list):
    for i in range(len(li)):
        if li[i] == '.':
            continue
        if li[i] in li[i + 1:]:
            return False
    return True


def check_row(li: list):
    for row in li:
        if basic_check(row) is False:
            return False

    return True


def check_col(li: list):
    n = len(li)

    for j in range(n):
        tmp_col = [li[x][j] for x in range(n)]
        if basic_check(tmp_col) is False:
            return False
    return True


def check_3x3(li: list):
    i = 0
    n = len(li)
    while i < n:
        j = 0
        while j < n:
            li_3x3 = li[i][j:j+3]
            li_3x3 += li[i+1][j:j+3]
            li_3x3 += li[i+2][j:j+3]

            # print(li_3x3)
            if basic_check(li_3x3) is False:
                return False

            j += 3
        i += 3
    return True


def check(li: list):
    if check_row(li) is False:
        return False
    if check_col(li) is False:
        return False
    if check_3x3(li) is False:
        return False
    return True


def main():
    # li = [
    #       [1, 2, 4],
    #       [4, 6, 2],
    #       [3, 4, 6]
    #       ]
    # print(li[1][:2])
    #
    # li1 = [1, 2, 3]
    # li2 = [3, 4, 5]
    # li1 += li2
    # print(li1)

    # print(check_3x3(li))
    # li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(check_3x3(li))
    # li = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
    #       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #       [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #       [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # print(check_3x3(li))
    li = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # print(check_3x3(li))

    # li = [[".",".",".",".","5",".",".","1","."],
    #       [".","4",".","3",".",".",".",".","."],
    #       [".",".",".",".",".","3",".",".","1"],
    #       ["8",".",".",".",".",".",".","2","."],
    #       [".",".","2",".","7",".",".",".","."],
    #       [".","1","5",".",".",".",".",".","."],
    #       [".",".",".",".",".","2",".",".","."],
    #       [".","2",".","9",".",".",".",".","."],
    #       [".",".","4",".",".",".",".",".","."]]
    print(check(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
