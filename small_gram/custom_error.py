# custom an error Class for small_gram
# python 3
# -*- coding: UTF-8 -*-


class CustomError(Exception):

    def __init__(self, info):
        self.error_info = info


class FunctionValueError(Exception):
    """这个类一旦出现，就代表你传入的函数参数有问题"""
    def __init__(self, info):
        self.error_info = info

    def __str__(self) -> str:
        return self.error_color['yellow']+self.error_info

    error_color = {'red': '\033[31;0m',
                   'green': '\033[32;0m',
                   'yellow': '\033[33;0m',
                   'blue': '\033[34;0m'}


def func_test(b):
    if b == 1:
        # raise CustomError
        raise FunctionValueError('{} is not good.'.format(b))


if __name__ == '__main__':
    import time
    print('-'*15, 'Start', time.ctime(), '-'*15, '\n')

    # txt color
    tc = {
        'red': '\033[31;0m',
        'green': '\033[32;0m',
        'yellow': '\033[33;0m',
        'blue': '\033[34;0m'
    }

    func_test(1)

    '''
    AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
 
    IOError 输入/输出异常；基本上是无法打开文件
     
    ImportError 无法引入模块或包；基本上是路径问题或名称错误
     
    IndentationError 语法错误（的子类） ；代码没有正确对齐
     
    IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
     
    KeyError 试图访问字典里不存在的键
     
    KeyboardInterrupt Ctrl+C被按下
     
    NameError 使用一个还未被赋予对象的变量
     
    SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
     
    TypeError 传入对象类型与要求的不符合
     
    UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
     
    ValueError 传入一个调用者不期望的值，即使值的类型是正确的
    '''
    print('%s%s %s %s %s' % ('\n', '-'*16, 'End', time.ctime(), '-'*16))
