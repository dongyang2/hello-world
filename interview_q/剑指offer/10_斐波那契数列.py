# 6,7,8,9都是C里面才有的数据结构的操作，Python里实现和操作都不太一样，这里先跳一跳

# coding: utf-8
# Python 3
# 这就是传说中的跳台阶，最最经典的动态规划。


def jump(n: int):
    if n < 0:
        raise ValueError()
    if n == 0:
        return 0
    if n == 1:
        return 1
    fn_2 = 0
    fn_1 = 1
    f = 0
    for i in range(1, n):
        f = fn_1 + fn_2
        fn_1, fn_2 = fn_1, f
    return f


def main():
    print(jump(4))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
