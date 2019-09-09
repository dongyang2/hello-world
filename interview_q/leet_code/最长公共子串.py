# https://leetcode-cn.com/problems/longest-common-prefix/
# utf-8
# Python 3


def longest_common_str(ss: list):
    ll = len(ss)
    lcs = ''  # longest_common_str

    if ll == 0:
        return lcs
    ls = len(ss[0])
    for i in range(ls):
        now_s = ss[0][i]
        bool_same = True
        for j in range(ll):
            if i < len(ss[j]):
                if ss[j][i] == now_s:
                    continue
                else:
                    bool_same = False
                    break
            else:
                bool_same = False
                break

        if bool_same is True:
            lcs += now_s
        else:
            break
    # print(lcs)
    return lcs


def main():
    li = ["flower", "flow", "flight"]
    # li = ["dog","racecar","car"]
    # li = ["aa", "a"]
    # li = ["aca","cba"]
    print(longest_common_str(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))