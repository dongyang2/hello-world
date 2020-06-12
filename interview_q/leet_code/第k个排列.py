# https://leetcode-cn.com/problems/permutation-sequence/
# coding: utf-8
# Python 3
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
# 指明 n 的范围是 [1, 9]。
# 指明 k 的范围是[1,  n!]。

# 思路：应该就是找下一个排列的问题。直接使用“下一个排列.py”文件的代码即可得到答案。
# 边界情况：空。

# 上面的思路超时了。
# 下面使用康托展开的思路。没学过密码学的应该对这个名词不熟悉。下面进行一定的介绍。
# 先抛出康托展开的公式。假设现在有n个数，f(x) = a_1*(n-1)! + a_2*(n-2)!+······+a_n*0! +1
# 然后解释一下这个公式，f(x)表示第x大的数，所以x取值范围在 1~n! ，
# a_1 到 a_n是什么呢？网上的解释模模糊糊就是在这里。下面一定要看清楚。举两个例子。
# a_1 到 a_n其实表示比当前排列的第i（0<i<n+1）个数字小，且还没有出现的个数。
# 以n=5为例，对排列54312而言，
# a_1是多少呢？此时i=1，排列54312的第1个数字是5，比5小的数字有4个，还没有出现的也有4个，所以a_1=4
# a_2是多少呢？此时i=2，排列54312的第2个数字是4，比4小的有3个，现在出现的数字是 4,5，有3个没出现，a_2=3
# a_3是多少呢？此时i=3，排列54312的第3个数字是3，a_3 = 2
# a_4是多少呢？此时i=4，排列54312的第4个数字是1，比1小的数字有0个，那么不用管还没出现几个了，a_4=0
# a_5是多少呢？此时i=5，排列54312的第5个数字是2，比2小的数字有1个，因为1已经出现了，所以a_5 = 0
# 计算f(x) = 4*4! + 3*3! + 2*2! + 0*1! + 0*0! + 1 = 119，那么这是12345这5个数字组成的全排列中按按字典序排序的第119个。最后一个当然是54321啦。
#
# 以n=4为例，对排列1324而言，
# a_1是多少呢？此时i=1，排列1324的第1个数字是1，比1小的数字有0个，那么不用管还没出现几个了，a_1=0
# a_2是多少呢？此时i=2，排列1324的第2个数字是3，比3小的有2个，现在出现的数字是 1，有1个没出现，a_2=1
# a_3是多少呢？此时i=3，排列1324的第3个数字是2，比2小的数字有1个，因为1已经出现了，所以a_3 = 0
# a_4是多少呢？此时i=4，排列1324的第4个数字是4，比4小的数字有3个，出现的数字是[1,3,2]，没出现的个数是0，那么a_4=0
# f(x) = 0*3!+1*2!+0*1!+0*0!+1 = 1*2+1 = 3，那么1324就是字典序排序的全排列中的第三个，前两个也容易写出来，是1234和1243.
#
# 通过上述例子，可以看到我们在已知排列的情况下，求该排列在字典序中是第几就很容易了。但题目是已知第几，求该排列。应该这么做？
# 很简单，填空法。设我们要求的是第k个排列，现在未知数是a_i，已知n，那么(n-1)!, (n-2)! ··· 1!就是已知的系数。
# 我们完全可以从a_1开始填空，即 (n-1)!*a_1 + (n-2)!*a_2 + ··· + 1!*a_n-1 + 0!*a_n + 1 = f(x) = k
# 有 (n-1)!*a_1 + (n-2)!*a_2 + ··· + 1!*a_n-1 + 0!*a_n = f(x) = k-1
# 下面举例说明，假设n=5,k=30，此时a_1~a_n如何求解（填空）？
# 此时上式变为 4!*a_1 + 3!*a_2 + 2!*a_3 + 1!*a_4 + 0!*a_5 = f(x) = 29
# 你可以想一下，如果k=24=4!，是不是刚好排列是15432 ？ k=25时，排列为21345，那么k=30时，第一位数肯定不是1，且我们大胆地猜它是2.
# 那么把它带进去4!*a_1 + 3!*a_2 + 2!*a_3 + 1!*a_4 + 0!*a_5 ，我们可以获得什么信息呢？
# a_1是多少呢？此时i=1，排列2xxxx的第1个数字是2，比2小的数字有1个，没出现的是1个，有a_1=1
# 代入方程得 4!*1 + 3!*a_2 + 2!*a_3 + 1!*a_4 + 0!*a_5 = f(x) = 29
# 化简得 3!*a_2 + 2!*a_3 + 1!*a_4 + 0!*a_5 = f(x) = 5
# 众所周知 3! = 6，那么我们大胆地猜a_2 = 0，那么第二位是什么数字才可以导致比他小还没出现的个数是0呢？
# 现在没有填的数字集合是{1,3,4,5}。试试填3，此时i=2，比3小的数字是[1,2]，出现了2，那么a_2 = 1，与前面a_2 = 0相冲突
# 那么只有1了。原方程变为 2!*a_3 + 1!*a_4 + 0!*a_5 = f(x) = 5 ，大胆得a_3 = 2，
# 可用集合为{3,4,5}，有第三位数为5。
# 更新方程，1!*a_4 + 0!*a_5 = f(x) = 1，大胆得到a_4 = 1，有第四位数为4，剩下一个3。
# 得最后结果21543。
# 由上述推论，启发式地得到填空方法。
# 设已知n，k，有li = [1,2,3,···,n]
# 先计算(k-1)/(n-1)! = tmp， 第一位数为li[tmp]，将li[tmp]弹出，
# 再计算((k-1)%(n-1)!)/(n-2)! = tmp，第二位数为li[tmp]，将li[tmp]弹出，
# 循环直到len(li) == 1.


def next_one(li: list):
    n = len(li)

    j = n-1
    while j != 0:
        if li[j] > li[j-1]:
            tmp = find_bigger_one_than_i(li, j-1)
            li[tmp], li[j-1] = li[j-1], li[tmp]
            sort_by_i(li, j-1)
            break
        j -= 1

    if j == 0:
        sort_by_i(li, -1)


def sort_by_i(li, i):
    # 把下标i之后的元素进行一次排序，且在当前数组中操作
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            if li[j] > li[k]:
                li[k], li[j] = li[j], li[k]


def find_bigger_one_than_i(li, i):
    # 找到仅仅比下标i的数字更大的数字的下标
    tmp = i+1
    for j in range(i+1, len(li)):
        if li[i] < li[j] < li[tmp]:
            tmp = j
    return tmp


def get_the_kth_one(n, k):
    if n < 1:
        return ""
    if n == 1:
        return "1"

    if k < 1 or k > factorial(n):
        return ""
    if k == 1:
        return "".join([str(x+1) for x in range(n)])

    li = [x+1 for x in range(n)]
    for _ in range(k-1):
        next_one(li)
    return "".join([str(x) for x in li])


def factorial(n: int):
    """计算n的阶乘"""
    tmp = 1
    for _ in range(n-1):
        tmp *= n
        n -= 1
    return tmp


def get_kth_one_cantor(n, k):
    if n < 1:
        return ""
    if n == 1:
        return "1"

    if k < 1 or k > factorial(n):
        return ""
    if k == 1:
        return "".join([str(x+1) for x in range(n)])

    li = [x+1 for x in range(n)]
    rest = k-1
    ans = ""
    for i in range(1, n+1):
        tmp = int(rest/factorial(n-i))  # 这里有重复计算，可以优化，但是n<=9，影响不大
        rest = rest % factorial(n-i)
        ans += str(li[tmp])
        li.pop(tmp)
    return ans


def main():
    # print(factorial(9))
    n = 4
    k = 9
    print(get_the_kth_one(n, k))
    print(get_kth_one_cantor(n, k))

    n = 5
    k = 30
    print(get_the_kth_one(n, k))
    print(get_kth_one_cantor(n, k))

    n = 9
    k = 138270
    # print(get_the_kth_one(n, k))
    print(get_kth_one_cantor(n, k))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
