# https://leetcode-cn.com/problems/palindrome-number/
# utf-8
# python3


def is_palindrome(x: int):
    s = str(x)
    if len(s) == 1:
        return True
    return s == str_reverse(s)


def str_reverse(s: str):
    """翻转字符串"""
    if s == '':
        return s
    tmp_s = ''
    for s_i in s[::-1]:
        tmp_s += s_i
    return tmp_s


def main():
    x = 10
    print(is_palindrome(x))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    main()

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
