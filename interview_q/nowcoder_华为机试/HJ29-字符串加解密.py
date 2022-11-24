#!python3
# coding:utf-8
import sys
import re
import copy


def encode(s: str, abc: str, num: str):
    n = len(s)
    encode_s = ''
    abc_up = abc.upper()
    for i in range(n):
        if s[i] in abc:
            ind = abc.index(s[i])
            if ind == 25:
                encode_s += 'A'
            else:
                encode_s += abc[ind + 1].upper()
        elif s[i] in abc_up:
            ind = abc_up.index(s[i])
            if ind == 25:
                encode_s += 'a'
            else:
                encode_s += abc_up[ind + 1].lower()
        elif s[i] in num:
            ind = num.index(s[i])
            if ind == 9:
                encode_s += '1'
            else:
                encode_s += num[ind + 1]
        else:
            encode_s += s[i]

    return encode_s


def decode(s: str, abc: str, num: str):
    n = len(s)
    encode_s = ''
    abc_up = abc.upper()
    for i in range(n):
        if s[i] in abc:
            ind = abc.index(s[i])
            if ind == 0:
                encode_s += 'Z'
            else:
                encode_s += abc[ind - 1].upper()
        elif s[i] in abc_up:
            ind = abc_up.index(s[i])
            if ind == 0:
                encode_s += 'z'
            else:
                encode_s += abc_up[ind - 1].lower()
        elif s[i] in num:
            ind = num.index(s[i])
            if ind == 0:
                encode_s += '0'
            else:
                encode_s += num[ind - 1]
        else:
            encode_s += s[i]

    return encode_s


def test1():
    abc = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    s = ""
    print(encode(s, abc, num))
    print(decode(s, abc, num))


def test2():
    s = "BabA "


def test3():
    s = "By?e"
    s = "gjo%%CGP-A+@-krz~dhxWb$qVev+!W^)~--U+ysdA^ZA~y^SxF!PUu&k"


def main():
    s1 = input().strip()
    s2 = input().strip()
    abc = "abcdefghijklmnopqrstuvwxyz"
    num = "1234567890"
    print(encode(s1, abc, num))
    print(decode(s2, abc, num))


if __name__ == '__main__':
    main()
