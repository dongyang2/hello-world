# https://leetcode-cn.com/problems/climbing-stairs/
# python 3
# utf-8


def clim(n: int):
    # 自底向上法
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    f1 = 1
    f2 = 2
    final = 0
    for _ in range(n)[2:]:
        final = f2+f1
        f2, f1 = final, f2
        # print(f2, f1)
    return final


def main():
    x = 3
    print(clim(x))


if __name__ == '__main__':
    import time
    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))