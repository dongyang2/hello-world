# https://leetcode-cn.com/problems/valid-parentheses/
# coding: utf-8
# Python 3
# 括号匹配
# 思路：栈
# 边界情况：没有括号，只有单个括号


def match_parentheses(s: str):
    li = []
    left_parentheses = ['(', '[', '{']
    for i in s:
        if i in left_parentheses:
            li.append(i)
        elif i == ')':
            if len(li) > 0:
                if li[-1] == '(':
                    li.pop()
                else:
                    return False
            else:
                return False
        elif i == ']':
            if len(li) > 0:
                if li[-1] == '[':
                    li.pop()
                else:
                    return False
            else:
                return False
        elif i == '}':
            if len(li) > 0:
                if li[-1] == '{':
                    li.pop()
                else:
                    return False
            else:
                return False

    if len(li) == 0:
        return True
    else:
        return False


def main():
    s = '''(])'''
    print(match_parentheses(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
