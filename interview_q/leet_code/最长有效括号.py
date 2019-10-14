# https://leetcode-cn.com/problems/longest-valid-parentheses/
# coding:utf-8
# Python 3


def max_kuo_hao(s: str):
    ls = len(s)
    stack = []
    for i in range(ls):
        if s[i] == ')' and len(stack)>0:
            if stack[-1][1] == '(':
                stack.pop(-1)
            else:
                stack.append([i, s[i]])
        else:
            stack.append([i, s[i]])

    count = 0
    ll = len(stack)
    if ll == 0:
        return ls

    j = 0
    tmp_count = 0
    for i in range(ls):
        if j < ll:
            if i == stack[j][0]:
                j += 1
                if tmp_count > count:
                    count = tmp_count
                tmp_count = 0
            else:
                tmp_count += 1
        else:
            tmp_count = ls-stack[j-1][0]-1
            if tmp_count > count:
                count = tmp_count

    return count


def main():
    # s = ")()())"
    s = "()(())"
    # s = "()(()"

    print(max_kuo_hao(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
