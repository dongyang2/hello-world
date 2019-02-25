# 这个程序必须要一个输入列表，打印这个输入列表的乱序输出且带有序号
# from small_gram import gen_random_order


def gen_random_order(num, seed=None):
    import random
    if seed is not None:
        random.seed(seed)
    li = list(range(num))
    random.shuffle(li)
    return li


if __name__ == '__main__':
    import time
    print('-'*16, 'Start', time.ctime(), '-'*16, '\n')

    li1 = ['33', '许婕', '松涛', 'Nick', '雨杰', '吴刚', '杨帆', 'Aloha', '思棋', '冬']  # 输入列表
    len_li = len(li1)
    order = gen_random_order(len_li, seed=319754)

    d = dict()
    for i in range(len_li):
        d[order[i]] = li1[i]

    print(d, '\n')
    s = '箭头代表送礼顺序 \n'
    for i in d:
        if i != len(d)-1:
            s += d[i]+' -> '
        else:
            s += d[i]
    print(s)
    
    print('\n', '-'*16, 'End', time.ctime(), '-'*16)
