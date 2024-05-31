#!python3
# coding: utf-8
# https://leetcode.cn/problems/fraction-to-recurring-decimal/
#
# 思路：
#
# 边界条件：


def add_zero(num1,num2):
    if len(str(num1)) < len(str(num2)):
        sub = len(str(num2)) - len(str(num1))
        return float(str(num1) +'0'*(sub+1))
    return float(num1)


def division(numerator:int, denominator:int):
    """计算小数的除法"""
    num = numerator//denominator
    numerator -= num
    tmps = ""

    while len(tmps) < 10000:
        num1 = add_zero(numerator, denominator)
        numerator = num1 // denominator
        tmps += numerator

    return str(num)+"."





def test():
    pass


def test1():
    # li = [11, 12,19]
    # print(bi_search(li, 20))

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20


def test2():
    numerator = 1
    denominator = 3333
    decimal = str(float(numerator * 1.0 / denominator))
    # print(len(decimal))
    print(add_zero(numerator, denominator))


def test3():
    matrix = [[]]
    target = 0
    # print(matrix[299][299])


def main():
    test2()


if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    start_time()
    main()
    end_time()
