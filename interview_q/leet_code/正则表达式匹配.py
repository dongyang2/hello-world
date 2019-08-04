# 失败

# https://leetcode-cn.com/problems/regular-expression-matching/
# utf-8
# python3


def match(s: str, p: str):
    l_s = len(s)
    l_p = len(p)
    if p == '':
        if s == '':
            return True
        return False
    elif p == '.*':
        return True
    elif s == '':
        if l_p == 2 and p[1] == '*':
            return True
        return False

    pi = 0
    si = 0
    while pi < l_p:
        s_for_match = p[pi]
        if s_for_match == '*':
            s_for_match = p[pi-1]

            if pi == l_p-1:
                if p[pi-1] == '.' or si == l_s:
                    return True
            else:
                if p[pi+1] == s_for_match or p[pi-1] == '.':
                    index = s.rfind(p[pi + 1])
                    if index == -1:
                        return False
                    else:
                        # print(s[index:], p[pi + 1:])
                        return match(s[index:], p[pi + 1:])

            while s_for_match == s[si]:
                si += 1
                if si == l_s:
                    break
            pi += 1

        elif s_for_match == '.':
            si += 1
            pi += 1
        elif s_for_match == s[si]:
            si += 1
            pi += 1
        elif pi != l_p-1:
            if p[pi+1] != '*':
                break
            else:
                pi += 1
        else:
            break

        if si == l_s:
            if pi < l_p:
                if p[pi] != '*':
                    break

    if si < l_s or pi < l_p:
        return False
    else:
        return True


def main():
    s = "a"
    p = "a*a"

    s = 'aaa'
    p = 'a*a'

    s = 'b'
    p = 'b*'

    s = "acaabbaccbbacaabbbb"
    p = "a*.*b*.*a*aa*a*"

    print(match(s, p))


if __name__ == '__main__':
    import time
    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
