#!python3
# coding: utf-8
# https://leetcode-cn.com/classic/problems/restore-ip-addresses/
# 给定一个只包含数字的字符串，复原它并返回所有可能的IP地址。
# 规定：s中仅有数字，长度 0<= len(s) <=3000
# （输入的字符串无效时，返回没有说明）
# 思路：切三刀，判定切出来的四段是否符合条件。
# 树的遍历，树深为4，每个节点最多只有3个子节点
# 注意：每切一刀都可以判定长度是否合理；0不能作为每段的开头


def ergodic_tree(daoshu: int, s: str, candidate: list, dao: int, last_dao: int, path: str):
    tmp_s = s[last_dao: dao]
    n = len(s)
    if len(tmp_s) > 1 and tmp_s[0] == "0":
        return
    if len(s[dao:]) > 3*(daoshu+1) or int(tmp_s) > 255:
        return

    if path == "":
        new_path = tmp_s
    else:
        new_path = path+"."+tmp_s
    if daoshu == 0:
        if dao == n:
            candidate.append(new_path)
    else:
        for i in range(dao+1, dao+4):
            if i < n+1:
                ergodic_tree(daoshu-1, s, candidate, i, dao, new_path)


def check_ip(s: str):
    n = len(s)
    if n < 4 or n > 12:
        return []

    candidate = []
    for dao in range(1, 4):
        ergodic_tree(3, s, candidate, dao, 0, "")
    return candidate


def main():
    # s = "12345"
    # s = "25525511135"
    # s = "0000"
    # s = "010010"
    s = "101023"
    # print(s[1:])
    print(check_ip(s))


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
