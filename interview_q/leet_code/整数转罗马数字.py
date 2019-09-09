# https://leetcode-cn.com/problems/integer-to-roman/
# utf-8
# python3


def int2rom(num: int):
    li = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
          (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'),
          (500, 'D'), (900, 'CM'), (1000, 'M')]

    s = ''
    while num>0:
        for i in range(len(li))[::-1]:
            if num - li[i][0] >= 0:
                num -= li[i][0]
                s += li[i][1]
                break
    print(s)
    return s


def main():
    num = 1994
    int2rom(num)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
