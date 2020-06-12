# https://leetcode-cn.com/problems/climbing-stairs/
# python 3
# utf-8
# 某人爬楼梯可以一次爬一阶或者两阶，问，n阶楼梯这人有几种爬法？
#
# 上个文件“爬楼梯.py”也是自己写的，这个文件为什么要命名为“爬楼梯_自己写”呢？
# 是因为上个文件过于久远且没有按照“题意-思路-边界条件”的格式来写，所以重写一次。
# 思路：其实倒着想就很简单，f(n) = f(n-1)+f(n-2)。那么，可以推广到某人可以一次跳m阶，
# 那么就有f(n) = f(n-1)+f(n-2)+f(n-3)+···+f(n-m)。既可用递归方法求解该式，又可使用迭代法进行求解。
# 要注意的是使用递归方法需要开辟一块空间记录求解过的值，避免重复运算。
# 边界条件：


def clim_recursive(n):
    """直接单纯地递归会在力扣上超时，在本地环境上（i5-7200U）求解输入为38的结果也会运行 11 秒。"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return clim_recursive(n-1) + clim_recursive(n-2)


def clim_iteration(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    f1 = 1
    f2 = 2
    for _ in range(n-2):
        tmp = f2+f1
        f1 = f2
        f2 = tmp
    return f2


def clim(n: int, rec: bool):
    """rec 是否使用迭代求解"""
    if n < 1:
        return 0
    if rec is True:
        li = [-1 for _ in range(n+3)]
        li[0] = 0
        li[1] = 1
        li[2] = 2
        return clim_recursive_with_memory_table(n, li)
    else:
        return clim_iteration(n)


def clim_recursive_with_memory_table(n, li):
    if li[n] == -1:
        li[n] = clim_recursive_with_memory_table(n-1, li) + clim_recursive_with_memory_table(n-2, li)
    return li[n]


def main():
    x = 4
    print(clim(x, rec=True))
    print(clim(x, rec=False))

    x = 38
    print(clim(x, rec=True))
    # print(clim(x, rec=False))

    x = 1
    print(clim(x, rec=True))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
