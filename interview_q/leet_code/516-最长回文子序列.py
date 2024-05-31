#!python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-palindromic-subsequence/description/
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
# 示例 1：
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#
# 示例 2：
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#
# #
# 思路：从题目可以看出只需要找到最长的长度即可，没有要求返回最长子序列本身，这就可以省很多时间。
#   设输入的字符串长度为n。
#   从删除0个字符开始，到删除1个字符。。。。。。到删除n个字符，如果删除1个字符找到了回文子序列，那么这个肯定是最长的，因为删除2个的肯定比它短。
#   所以走广度优先遍历。
# !!! 注意广度优先遍历是用队列迭代实现的，而非递归。!!!
#


def mirror(s: str):
    """判定是否对称"""
    l = len(s)
    if s[:int(l / 2)] == s[:int((l - 1) / 2):-1]:
        return True
    return False


def longest_str(s: str):
    """最初的想法——广度优先遍历"""
    if mirror(s):
        return len(s)
    else:
        li = [s]
        while li:
            node = li.pop(0)
            for i in range(len(node)):
                fn_1 = node[:i] + node[i + 1:]
                if mirror(fn_1):
                    return len(node) - 1
                li.append(fn_1)


def main():
    # s = "abcdacba"
    # s = "bbbab"
    # s = "cbbd"
    s = "abcabcabcabc"
    s = "abcdabcdabcdabcd"  # 如果直接使用广度优先遍历，超出时间限制
    print(longest_str(s))


if __name__ == '__main__':
    main()
