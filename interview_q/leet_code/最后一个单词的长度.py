# https://leetcode-cn.com/problems/length-of-last-word/
# coding: utf-8
# Python 3
# 输入一个字符串。每一个单词由空格分开。且指定单词只由字母组成。不存在最后一个单词的情况返回0.
#
# 思路：因为Python自带字符串的各种操作，所以分为两个版本，一个是py版，一个是普通版。
# 边界条件：最后一个子串里有非字母。空字符串输入。空格在最后。


def get_last_word_length(s):
    """普通版，遍历字符串的同时维护一个变量last_one"""
    if s == "":
        return 0

    n = len(s)
    if s[n-1] == " ":  # 先把后面的空格去掉
        count = 0
        for i in range(n):
            if s[n-1-i] == " ":
                count += 1
            if s[n-1-i] != " ":
                break
        tmp = ""
        for i in range(n-count):
            tmp += s[i]
        s = tmp

    last_one = ""
    for i in s:
        if i == " ":
            last_one = ""
        else:
            last_one += i
    if word_valid(last_one) is False:
        return 0
    return len(last_one)


def word_valid(s):
    """判断单词是否符合规范"""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        if i not in alphabet:
            return False
    return True


def get_last_word_length_py(s: str):
    if s == "":
        return 0
    s = s.strip()
    last_one = s.split(" ")[-1]
    if word_valid(last_one) is False:
        return 0
    return len(last_one)


def main():
    # s = "hello world!"
    # s = "a "
    s = " a "
    print(get_last_word_length(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
