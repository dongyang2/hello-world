# https://leetcode-cn.com/problems/group-anagrams/
# coding: utf-8
# Python 3
# 给定一个字符串数组，将所有字母相同，但排列不同的字符串放在一起。
#
# 思路：建立字典收集字母相同的字符串。
# 边界条件：
#
# 网上的思路：利用字母出现次数进行计数，计数相同的就可以划在一组。
# 虽然自己的思路很快，力扣 48ms，但是我不想使用sorted()函数。上面这一行的思路更符合我口味。


def group_same_letter(li: list):
    candidate = dict()
    for i in li:
        s_l = sorted(i)
        s_l_union = ''.join(s_l)
        if s_l_union in candidate:
            candidate[s_l_union].append(i)
        else:
            candidate[s_l_union] = [i]
    group = [candidate[k] for k in candidate]
    return group


def group_same_letter_by_count(li):
    """网上的思路实现。力扣 1928ms"""

    # 造一个字典，用于后面的计数
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abc_dic = dict()
    for i in range(26):
        abc_dic[alphabet[i]] = i

    count_li = []
    group = []
    for i in li:
        count_num = make_count_number(i, abc_dic)
        if count_num in count_li:
            ind = count_li.index(count_num)
            group[ind].append(i)
        else:
            count_li.append(count_num)
            group.append([i])

    return group


def make_count_number(s, abc_dic):
    """统计一个字符串中所有字符出现的次数，并以数组形式返回统计结果"""
    tmp_li = [0 for _ in range(26)]
    for i in s:
        tmp_li[abc_dic[i]] += 1

    return tmp_li


def main():
    li = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(group_same_letter(li))

    print(group_same_letter_by_count(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
