# https://leetcode-cn.com/problems/simplify-path/
# coding: utf-8
# Python 3
# 输入是绝对路径，里面包含了返回上一目录的操作，输出是操作后的绝对路径。
# 规定在根目录使用..进行返回上一目录的操作，输出为根目录。规定最后一个目录后不跟/。
#
# 思路：栈。
# 边界条件：空输入。


def normalize_path(path: str):
    """"""
    n = len(path)
    if n == 0:
        return "/"
    final_path = []
    start = 0
    path += "/"   # 这句话是为了把path的长度变成n+1，但是下面的遍历到n就结束了。
    for i in range(n):
        if path[i] == "/":
            if path[i+1] != "/":
                start = i+1
        else:
            if path[i+1] == "/":
                mid = path[start: i+1]
                if mid == "..":
                    if len(final_path) != 0:
                        final_path.pop(-1)
                elif mid != ".":
                    final_path.append(mid)

    return "/"+"/".join(final_path)


def main():
    s = "/home//foo/"
    print(normalize_path(s))

    s = "/a/./b/../../c/"
    print(normalize_path(s))

    s = "/a/../../b/../c//.//"
    print(normalize_path(s))

    s = "/../"
    print(normalize_path(s))

    s = "/a//b////c/d//././/.."
    print(normalize_path(s))

    s = "/home/"
    print(normalize_path(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
