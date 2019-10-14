# https://leetcode-cn.com/problems/regular-expression-matching/
# utf-8
# python3


def match(s: str, p: str, i=0, j=0, m=None):
    # print(m, i, j)
    ls = len(s)
    lp = len(p)

    if i == ls and j == lp:
        return True

    if i == ls and j != lp:
        # 字符串跑完了但是pattern没跑完
        if j < lp - 1:
            if p[j + 1] == '*':
                return match(s, p, i, j + 2, m='忽')
        return False

    # if i == ls-1 and j == lp-1 and p[j]!='*':
    #     if s[i] == p[j] or p[j]=='.':
    #         return True
    #     else:
    #         return False

    # pattern的下个是'*'
    if j < lp - 1:
        if p[j + 1] == '*':
            if p[j] == s[i] or (p[j] == '.' and i != ls):
                # print('匹配上了')
                # 进入有限状态机的下一个状态 或者 停在当前状态 或者 忽略‘*’
                return match(s, p, i + 1, j + 2, m='下个状态') or match(s, p, i + 1, j,
                                                                    m='状态停留') or match(s, p, i, j + 2, m='忽略')
                # if s[i + 1] == p[j]:
                #     return match(s, p,  i + 1, j, m='停留') or match(s, p, i, j + 2, m='忽略')
                # else:
                #     return match(s, p,i + 1, j + 2, m='下个') or match(s, p, i, j + 2, m='忽略')
            else:
                # print('没匹配上')
                # 匹配0次，直接忽略‘*’
                return match(s, p, i, j + 2)

    # pattern的下个不是'*'
    if i < ls and j < lp:
        if s[i] == p[j] or p[j] == '.':
            return match(s, p, i + 1, j + 1)

    return False


def del_redundant_star(s: str):
    ls = len(s)

    tmp_s = ''
    bool_r = False
    for k in range(ls):
        if s[k] == '*' and k < ls - 1:
            if s[k - 1] == s[k + 1]:
                if k < ls - 2:
                    if s[k + 2] == '*':
                        tmp_s = s[:k - 1] + s[k + 1:]
                        bool_r = True

    if bool_r is True:
        s = del_redundant_star(tmp_s)

    return s


def main():
    s = "a"
    p = "a*a"

    # s = 'aaa'
    # p = 'a*a'

    # s = 'b'
    # p = 'b*'

    # # s = "acaabbaccbbacaabbbb"
    # s = "acaabbaccbbacaa"
    # p = "a*.*b*.*a*aa*a*"

    # s = "aa"
    # p = "a*"

    # s = 'ab'
    # p = '.*'

    # s = "ssissippi"
    # p= "s*is*ip*."

    # s = 'a'
    # p = 'ab*'

    # s = "aaaaaaaaaaaaab"
    # p = "a*a*a*b*b*b*b*a*a*c*c*c*c*d*e*f*g*a*c"

    li = []
    n = len(s)
    m = len(p)
    for _ in range(n):
        tmp = []
        for __ in range(m):
            tmp.append(None)
        li.append(tmp)

    p = del_redundant_star(p)
    print(p)
    print(match(s, p))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
