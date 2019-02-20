def all_zero(path):
    import numpy as np
    wno = np.loadtxt(path, delimiter=',', encoding='utf-8', dtype=str)
    len_zero = len(wno[:, 2]) - 1
    zero = np.zeros(len_zero, np.int).astype(str)
    col = np.array([wno[:, 2][0]])
    col = np.append(col, zero)

    li_0 = wno[:, 0]
    li_3 = wno[:, 3]
    li_1 = wno[:, 1]
    result = [li_0, li_1, col, li_3]
    result = np.array(result).T

    w_path = rename(path, '_00')
    with open(w_path, 'w', encoding='utf-8')as f:
        for i in result:
            s = ','.join(i)
            f.write(s + '\n')


def rename(di, add):
    tmp = di.split('.')
    s = tmp[0] + add
    li = [s, tmp[1]]
    return '.'.join(li)


def handle_ft_predict_result(li):
    new_li = []
    # s = li[0][0].split('__label__')[1:]
    # score = li[1][0]
    i = 0
    while i < len(li[0]):
        sub_lab = li[0][i].split('__label__')[1:]
        sub_lab.append(li[1][i])
        new_li.append(sub_lab)
        i += 1
    # print(s, score)
    import numpy as np
    print(np.array(new_li))
    return np.array(new_li)


if __name__ == '__main__':
    # all_zero("E:/桌面/word_ngram_over_1.csv")

    a = (('__label__价格,__label__0', '__label__配置,__label__0', '__label__舒适性,__label__0', '__label__内饰,__label__0',
          '__label__操控,__label__0', '__label__外观,__label__0', '__label__价格,__label__1', '__label__价格,__label__-1',
          '__label__外观,__label__-1', '__label__空间,__label__0'), (
             [0.65184933, 0.13537788, 0.03864675, 0.03446486, 0.02373006,
              0.01929222, 0.01810671, 0.01399508, 0.00904865, 0.00893954])
         )
    handle_ft_predict_result(a)
