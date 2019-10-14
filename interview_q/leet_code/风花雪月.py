# coding:utf-8
# Python 3


def happy_game(n: int, li_m, li_c):
    li = [0 for _ in range(n)]
    lm = len(li_m)

    if li_m != [None]:
        for i in range(lm-1):
            if li_m[i+1] - li_m[i] == 1 and li_c[i+1] == li_c[i]:
                return 0

        # 将m 的值输入到li 中
        for i in range(lm):
            wi = li_m[i]
            li[wi-1] = li_c[i]
        print(li)

    count = 1
    last_num = 0
    for i in range(n):
        if li[i] != 0:
            continue
        else:
            if i ==0:
                if li[1] == 0:
                    num_prob = 4
                else:
                    num_prob = 3
            elif i == n-1:
                num_prob = 3
            else:
                if li[i-1] != 0 and li[i+1 ] != 0 and li[i-1] != li[i+1]:
                    num_prob = 2
                elif (li[i-1] == 0 and li[i+1] != 0) or (li[i-1] != 0 and li[i+1] == 0):
                    count /= last_num
                    num_prob = 6
                else:
                    num_prob = 3
        last_num = num_prob
        count *= num_prob
    # print(count)
    return int(count)


def main():
    m = [1,2]
    # m = [None]
    n = 10
    c = [1,1]

    n = 1000
    m = [None]

    n = 12
    m = [4, 8 ,12]
    c = [3, 3, 3]
    ans = happy_game(n, m, c)
    print(ans)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))






