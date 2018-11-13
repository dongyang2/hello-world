def get_dir(fil_nam):
    """获得文件的整个目录"""
    s = fil_nam.split('/')[:-1]
    tmp_s = ''
    for i in s:
        tmp_s += i + '/'
    return tmp_s


def get_sub_or_elem(si, li):
    """si 表示str or int，输入是字符串时返回下标，输入整数时返回对应字符串"""
    if isinstance(si, str):
        return li.index(si)
    elif isinstance(si, int):
        return li[si]


if __name__ == '__main__':
    names = ['丰水梨', '冰糖心苹果', '冰糖橙', '台湾青枣', '国产青苹果', '大台农芒', '富士王', '小台农芒', '泰国香蕉', '海南香蕉', '澳洲大芒', '澳洲蜜柑', '特级红富士',
             '番石榴', '百香果', '砀山梨', '米蕉', '纽荷脐橙', '脆肉瓜', '花牛红苹果', '蜜梨', '贡梨', '陕西香酥梨', '雪梨', '鸭梨', '黄金梨']
    print(get_sub_or_elem('冰糖心苹果', names))
    print(get_sub_or_elem(3, names))
