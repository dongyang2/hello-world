# https://leetcode-cn.com/problems/reverse-integer/
# utf-8
# python3


def integer_reverse(x: int):
    """x是有符号32位整数"""
    if not bool_int32(x):
        return 0
    s_x = str(x)
    sign = ''
    if s_x[0] == '-':
        sign = '-'
        s_x = s_x[1:]
    reversed_x = int(sign+str_reverse(s_x))
    if not bool_int32(reversed_x):
        return 0
    return reversed_x


def bool_int32(i: int):
    """判断是否在int32范围内"""
    if i < pow(-2, 31) or i > pow(2, 31)-1:
        return False
    else:
        return True


def str_reverse(s: str):
    """翻转字符串"""
    if len(s) == 0:
        raise ValueError('请输入非空字符串')
    tmp_s = ''
    for s_i in s[::-1]:
        tmp_s += s_i
    return tmp_s


def main():
    s = 1534236469

    print(integer_reverse(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    main()

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
