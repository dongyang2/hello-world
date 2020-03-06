# https://leetcode-cn.com/problems/longest-valid-parentheses/
# coding:utf-8
# Python 3
# 思路：先把输入字符串分为两种情况，一种是全部合法的括号，另一种是被“（”或者“）”分割的若干个合法括号子段。
# 由此，先设立一个栈，把合法的括号对都清理掉，留下不合法的“（”或“）”的位置信息，
# 再根据位置信息计算各个合法括号子段的长度，进行对比，求出最长合法子段的长度。


def max_kuo_hao(s: str):
    ls = len(s)  # 输入字符串的长度
    stack = []
    for i in range(ls):
        if s[i] == ')' and len(stack) > 0:
            if stack[-1][1] == '(':
                stack.pop(-1)
            else:
                stack.append([i, s[i]])
        else:
            stack.append([i, s[i]])

    count = 0
    ll = len(stack)  # 栈的长度
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


def max_parentheses(s: str):
    # 根据上面的max_kuo_hao函数进行改进。在力扣上测试速度加快40%
    ls = len(s)  # 输入字符串的长度
    stack = []
    for i in range(ls):
        if s[i] == ')' and len(stack) > 0:
            if stack[-1][1] == '(':
                stack.pop(-1)
            else:
                stack.append([i, s[i]])
        else:
            stack.append([i, s[i]])

    ll = len(stack)  # 栈的长度
    if ll == 0:
        return ls

    max_len = stack[0][0]
    for i in range(ll):
        if i == ll-1:
            tmp = ls-stack[-1][0]-1
        else:
            tmp = stack[i+1][0]-stack[i][0]-1
        if tmp > max_len:
            max_len = tmp

    return max_len


def main():
    # s = ")()())"
    # s = "()(())"
    s = "()(()(()"

    # print(max_kuo_hao(s))
    print(max_parentheses(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
