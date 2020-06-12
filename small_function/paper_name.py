# coding: utf-8
# 哈工大毕业论文，参考文献论文名称要求。
# Python 3


def upper_1st_char_in_real_word(p_name):
    # 实词首字母大写
    function_word = ['above', 'against', 'along', 'among', 'another', 'around', 'as', 'at', 'before',
                     'behind', 'below', 'beneath', 'besides', 'between', 'beyond', 'but', 'by', 'concerning',
                     'considering', 'despite', 'down', 'during', 'except', 'excepting', 'excluding', 'flowing', 'for',
                     'from', 'front', 'in', 'including', 'inside', 'into', 'like', 'near', 'next', 'of', 'on', 'onto',
                     'or', 'over', 'since', 'till', 'to', 'up', 'via', 'while', 'with', 'within', 'without',
                     'when', 'yet', 'thus', 'that', 'than', 'so', 'if', 'once', 'never', 'and', 'also', 'would',
                     'could', 'might', 'must', 'shall']
    s = ''
    for i in p_name.split(' '):
        if i not in function_word:
            if '-' in i:
                s += '-'.join([upper_1st(j) for j in i.split('-')]) + ' '
            else:
                s += i.capitalize()+' '
        else:
            s += i+' '
    return s


def upper_1st(s: str):
    return s[0].upper()+s[1:]


def main():
    # s = 'ImageNet classification with deep convolutional neural networks'
    # 可以把参考文献一并放入下面这个变量，运行完后只复制论文名称过去就行，注意复制过去后Word会给你加一个空格，要删掉。
    s = '''参考文献'''

    print(upper_1st_char_in_real_word(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
