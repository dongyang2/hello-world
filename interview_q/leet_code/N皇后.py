# https://leetcode-cn.com/problems/n-queens/
# coding: utf-8
# Python 3
# 著名的八皇后问题的衍生款。给定一个n*n的棋盘，求n个皇后在里面互相不攻击的所有可能摆法。
# 皇后的攻击范围是横、竖、平行于对角线的斜。
#
# 思路：这题主要考察答题者对数组的熟练程度。同时还要考虑遍历树的时候进行回溯。
# 自己画了边长为1~5的棋盘，发现2*2和3*3的没有解，题中没有给出解释无解时返回什么，暂时以返回空数组处理。
# 棋盘解法都是对称的。
# 根据自己画的过程，得到解题方法，先摆第一行的，再摆第二行的，如果摆到了最后一行，则存为一个解，否则无解。
# 边界条件：


def n_queens(n):
    if n == 0 or n == 2 or n == 3:
        return []  # 好吧，不是[[]]，是[]
    if n == 1:
        return [['Q']]

    ans = []
    board = make_board(n)
    for first_i in range(n):
        # put_a_queen(board, 0, i)
        ergodic_tree(put_a_queen(board, 0, first_i), 0, ans)
    return post_process(ans)


def ergodic_tree(board, floor, ans):
    """遍历这颗树有两个终止条件，一是棋盘到最后一行了（有解），二是没有可以摆的位置了。（无解）"""
    if "." in board[floor + 1]:
        n = len(board)
        if floor+1 == n-1:  # 到最后一层了
            ind = board[floor + 1].index(".")
            board[floor + 1][ind] = "Q"
            ans.append(board)
        else:
            for k in range(n):
                if board[floor + 1][k] != "-":
                    ergodic_tree(put_a_queen(board, floor + 1, k), floor + 1, ans)


def make_board(n):
    """造棋盘"""
    li = []
    for _ in range(n):
        li.append(["." for _ in range(n)])
    return li


def put_a_queen(li, i, j):
    """和以往的遍历树一样，这里需要重新申请一块空间用于遍历各种可能"""
    new_li = []
    for row in li:
        tmp = [str(x) for x in row]
        new_li.append(tmp)

    n = len(li)
    for k in range(n):  # 同时设定横竖两条线
        new_li[i][k] = "-"
        new_li[k][j] = "-"
    rest = min(n-j, n-i)  # 看行与列谁剩的少
    for k in range(1, rest):  # 设定斜的一条线
        new_li[i+k][j+k] = "-"
    rest = min(j+1, n-i)
    for k in range(1, rest):  # 设定斜的另一条线
        new_li[i+k][j-k] = "-"
    new_li[i][j] = "Q"
    return new_li


def flip(li):
    """将数组沿竖轴翻转赋值给新数组"""
    new_li = []
    n = len(li)
    for row in li:
        tmp_li = [row[n-x-1] for x in range(n)]
        new_li.append(tmp_li)
    return new_li


def see_see(board):
    for i in board:
        for row in i:
            print(row)
        print(',')


def post_process(board):
    new_li = []
    for i in board:
        tmp_li = []
        for row in i:
            tmp_s = ""
            for j in row:
                if j == "-":
                    tmp_s += "."
                else:
                    tmp_s += j
            tmp_li.append(tmp_s)
        new_li.append(tmp_li)
    return new_li


def main():
    # print(make_board(3))
    # li = make_board(5)
    # nl = put_a_queen(li, 2, 3)
    # for row in nl:
    #     print(row)
    # put_a_queen(li, 1, 2)
    # print(li)

    see_see(n_queens(4))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
