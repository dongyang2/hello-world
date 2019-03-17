# 更改需要过滤的国内链接以适用于其他浏览器


def change_url(s):
    new_f = []
    for i in s:
        j = i.split(';')
        # print(j)
        for k in j:
            if k != '':
                new_f.append(k+'\n')
    return new_f


def change_url_new(s, to_s):
    import re
    pattern = re.compile(r';')
    return re.sub(pattern, to_s, s)


if __name__ == "__main__":
    import argparse
    import os
    import sys
    now_path = os.getcwd()
    dir_path = '/'.join(now_path.split('\\')[:-1])
    sys.path.append(dir_path)  # 把这个加入环境变量

    from small_gram import read_file_to_str, write_file, get_dir

    explorer_name_choice = ['360', 'firefox']
    parser = argparse.ArgumentParser(description='change the filtered url to other explorer\'s format')

    parser.add_argument('input', metavar='the input', help='The input must be a file or a string.')
    parser.add_argument('name', metavar='explorer name', choices=explorer_name_choice, help='The explorer\'s name.')
    parser.add_argument('--out', '-o', metavar='output dir',
                        help='Output directory. If not exits will save result to the input file\'s directory.'
                             ' If input is not a file, save to this script\'s directory.',
                        default=False)
    args = parser.parse_args()

    fi_or_s = args.input

    d = {'360': '\n', 'firefox': ','}
    need_s = d[args.name]

    if os.path.exists(fi_or_s):  # 先判断是否为文件
        origin_s = read_file_to_str(fi_or_s)
        file_dir = get_dir(fi_or_s)
    elif isinstance(fi_or_s, str):  # 不是文件就按照字符串处理
        origin_s = fi_or_s
        file_dir = './'  # 如果输入不是文件，则在后续需要保存时放在本程序所在目录下
    else:
        raise IOError('Input must be a string or file path')

    new_s = change_url_new(origin_s, need_s)
    if args.out:
        if os.path.isdir(args.out):  # 判断是否是文件夹，是的话就存在那，否则存到输入文件所在文件夹。
            output_dir = args.out+'url_'+args.name+'.txt'
        else:
            output_dir = file_dir+'url_'+args.name+'.txt'
        write_file(new_s, output_dir, '1D list')
        print('保存完毕。')
    else:
        print(new_s)
