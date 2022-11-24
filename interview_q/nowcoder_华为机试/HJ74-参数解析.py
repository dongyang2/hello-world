#!python3
# coding: utf-8

import sys
import re
import copy


def parse(inps: str):
    stack = []
    word = ""
    li = []
    for i in range(len(inps)):
        if inps[i] == "\"":
            if stack:
                stack.pop()
                li.append(word)
                word = ""
            else:
                stack.append("\"")
        else:
            if len(stack) == 0:
                if inps[i] == " ":
                    if word != "":
                        li.append(word)
                        word = ""
                else:
                    word += inps[i]
            else:
                word += inps[i]
    if word != "":
        li.append(word)
    print(len(li))
    print("\n".join(li))


def test1():
    abc = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    s = """xcopy    "/s" c:\\ d:\\e"""  # 注意这里的输入案例，和input()函数接收到的格式不一样，这里的符号会被转义，而input()接收到的不会
    parse(s)


def test2():
    s = "a "
    parse(s)


def test3():
    s = "By?e"
    s = """xcopy "/s" "C:\\program files" d:\\e"""
    parse(s)


def main():
    abc = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"

    s1 = input().strip()
    parse(s1)

    # test3()


if __name__ == '__main__':
    main()
