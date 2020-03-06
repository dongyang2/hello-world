# https://leetcode-cn.com/problems/implement-strstr/
# coding: utf-8
# Python 3
# 实现python 3中字符串操作的find()函数
# 思路：
# 边界情况：


def find_imitate(s: str, key: str):
    if key == '':
        return 0

    n = len(s)
    m = len(key)
    for i in range(n):
        if s[i] == key[0]:
            tmp = i+1
            if tmp+m-1 > n:  # 如果后面没有足够的字符了，就直接返回找不到了
                return -1
            j = 1
            while j < m:
                if s[tmp] != key[j]:
                    break
                j += 1
                tmp += 1
            if j == m:
                return i
    return -1


def main():
    s = 'cbbbba'
    key = 'bba'
    print(find_imitate(s, key))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
