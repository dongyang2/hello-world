# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
# coding: utf-8
# Python 3


def combination(digits: str):
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'

    }
    if len(digits) == 0:
        return []

    s_li = ['']  # 这里的''元素很关键，是循环加入的开始，不然后面无法遍历加元素进来
    for i in digits:
        tmp = []
        for j in dic[i]:
            for k in s_li:
                tmp.append(k + j)
        s_li = tmp
    return s_li


def main():
    d = '23'

    print(combination(d))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
