# https://leetcode-cn.com/problems/roman-to-integer/
# utf-8
# Python 3


def roma2int(s: str):
    num = 0
    ls = len(s)
    i = 0
    while i < ls:
        if s[i] == 'I':
            if i != ls - 1:
                if s[i + 1] == 'V':
                    num += 4
                    i += 1
                elif s[i + 1] == 'X':
                    num += 9
                    i += 1
                else:
                    num += 1
            else:
                num += 1
        elif s[i] == 'V':
            num += 5
        elif s[i] == 'X':
            if i != ls - 1:
                if s[i + 1] == 'L':
                    num += 40
                    i += 1
                elif s[i + 1] == 'C':
                    num += 90
                    i += 1
                else:
                    num += 10
            else:
                num += 10
        elif s[i] == 'L':
            num += 50
        elif s[i] == 'C':
            if i != ls - 1:
                if s[i + 1] == 'D':
                    num += 400
                    i += 1
                elif s[i + 1] == 'M':
                    num += 900
                    i += 1
                else:
                    num += 100
            else:
                num += 100
        elif s[i] == 'D':
            num += 500
        else:
            num += 1000
        i += 1

    # print(num)
    return num


def main():
    s = 'LVIII'
    roma2int(s)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
