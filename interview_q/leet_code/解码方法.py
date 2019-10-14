# https://leetcode-cn.com/problems/decode-ways/
# coding:utf-8
# Python 3
# 数字与字母一一对应，求转换结果。解法参考本文件夹下的爬楼梯和电话号码的字母组合。
"""
此题和爬楼梯是同一个类型的问题，难点在于其添加了许多限制条件，只要避开限制条件就可以完美解题了

每次递进，可以选取一个数也可以选取两个数：

    s[i] != '0'

    如果 s[i-1]s[i] <= 26, 则 dp[i] = dp[i-1] + dp[i-2]
    如果 s[i-1]s[i] > 26, 则 dp[i] = dp[i-1], 这是因为 s[i-1]s[i] 组成的两位数无法翻译

    s[i] == '0'

    如果 s[i-1]s[i] <= 26, 则 dp[i] = dp[i-2], 这是因为 s[i] 无法翻译

    还有一些情景直接使得整个序列无法被翻译：

    相邻的两个 ‘0’
    以 ‘0’ 结尾的大于 26 的数字

去除这些限制条件，此题就是爬楼梯的问题了，一次可以爬一步，也可以爬两步，问有多少中方式到达终点。

作者：nfgc
链接：https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-tu-jie-by-nfgc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# 除了解题思路以外，还要注意‘10’，‘00’, '101','301'这样的边界输入


def clim(s, dic):
    """有条件的爬楼梯，自底向上法"""
    ln = len(s)

    if ln < 1 or s[0] == '0':
        return 0
    if ln == 1:
        if s == '0':
            return 0
        return [dic[s]]

    li1 = [dic[s[0]]]
    li2 = decode_2char(s[:2], dic)
    if li2 is False:
        return 0

    for i in range(2, ln):
        tmp = []  # 充当爬楼梯中的final
        two_char = s[i - 1] + s[i]
        if s[i] != '0':
            if int(two_char) <= 26 and s[i - 1] != '0':
                tmp = decode(two_char, li1, tmp, dic)
                tmp = decode(s[i], li2, tmp, dic)
            else:
                tmp = decode(s[i], li2, tmp, dic)
        else:
            if s[i - 1] == '1' or s[i - 1] == '2':
                tmp = decode(two_char, li1, tmp, dic)
            else:
                return 0
        li1, li2 = li2, tmp
    return li2


def decode_2char(n, dic):
    # 解码两位数字
    s1 = n[0]
    s2 = n[1]
    if s2 == '0':
        if s1 == '1' or s1 == '2':
            return [dic[n]]
        else:
            return False
    li = [dic[n[0]] + dic[n[1]]]
    if int(n) <= 26:
        li.append(dic[n])
    return li


def decode(s: str, li: list, tmp: list, dic):
    for i in li:
        tmp.append(i + dic[s])
    return tmp


def clim_pure_num(s):
    """有条件的爬楼梯，自底向上纯计数方式，不收集元素"""
    ln = len(s)

    if ln < 1 or s[0] == '0':
        return 0
    if ln == 1:
        return 1

    f1 = 1
    f2 = decode_2char_pure_num(s[:2])
    if f2 is False:
        return 0

    for i in range(2, ln):
        two_char = s[i - 1] + s[i]
        if s[i] != '0':
            if int(two_char) <= 26 and s[i - 1] != '0':
                final = f1 + f2
            else:
                final = f2
        else:
            if s[i - 1] == '1' or s[i - 1] == '2':
                final = f1
            else:
                return 0
        f1, f2 = f2, final
    return f2


def decode_2char_pure_num(n):
    # 解码两位数字，配合纯数字版
    s1 = n[0]
    s2 = n[1]
    if s2 == '0':
        if s1 == '1' or s1 == '2':
            return 1
        else:
            return False
    if int(n) <= 26:
        return 2
    else:
        return 1


def main():
    dic = dict()
    count = 1
    upper_abc = [chr(65 + x) for x in range(26)]
    for i in upper_abc:
        dic[str(count)] = i
        count += 1
    # print(dic)
    n = "27"
    # li = clim(n, dic)
    li = clim_pure_num(n)
    if li == 0:
        raise ValueError('Please input valid number.')
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    # print(str(int('00000000235600000')))
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
