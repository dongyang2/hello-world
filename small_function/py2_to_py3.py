# 将python2文件转为python3文件，最常见的就是print bla~bla~bla~ 了，还有修改一些库的导入，可以持续更新
# urllib2可以直接通过替换成urllib.request来用，与此同时，urlib.encode要换成from urllib.parse import urlencode


def turn_print(f_path):
    s = ''
    with open(f_path, mode='r', encoding='utf-8') as f:
        for i in f:
            ind = i.find('print')
            if ind != -1:
                tmp = i.split(' ')[1:]
                blank = ''
                for j in range(ind):
                    blank += ' '
                tmp_s = blank+'print('
                for j in tmp:
                    if j != '':
                        tmp_s += j+' '
                tmp_s = tmp_s[:-1]+')'
                s += tmp_s
            else:
                s += i
    with open(f_path, mode='w', encoding='utf-8') as f:
        f.write(s)


if __name__ == '__main__':
    path1 = 'E:/常用文档/日志/181112.txt'
    turn_print(path1)
