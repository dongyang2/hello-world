# https://leetcode-cn.com/problems/string-to-integer-atoi/
# utf-8
# python3


def atoi(s: str):
    integer_list = '1234567890'
    s = s.strip()
    if s == '':
        return 0

    # 针对正负号做工作
    sign = ''
    if s[0] == '+':
        s = s[1:]
    elif s[0] == '-':
        if len(s) == 1:
            return 0
        elif s[1] not in integer_list:
            return 0
        sign = '-'
        s = s[1:]

    # 找出连续数字
    index = len(s)
    for i in range(len(s)):
        if s[i] not in integer_list:
            index = i
            break

    int_s = sign+s[:index]
    if int_s == '' or int_s == '-' or int_s == '+':
        return 0
    integer = int(int_s)
    return bool_int32(integer)


def bool_int32(i: int):
    """限制i在int32范围内"""
    if i < pow(-2, 31):
        return pow(-2, 31)
    elif i > pow(2, 31)-1:
        return pow(2, 31)-1
    else:
        return i


def main():
    s = "-91283472332"

    print(atoi(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    main()

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
