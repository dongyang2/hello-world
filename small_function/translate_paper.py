﻿# coding: utf-8
# pip install PyExecJS
# pip install bs4
# pip install requests

import urllib.parse
import execjs
import requests


class FunctionValueError(Exception):
    def __init__(self, info):
        self.error_info = info

    def __str__(self) -> str:
        return '\033[33;0m'+self.error_info


class ReturnTk:

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < 
            a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? 
            (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def get_tk(self, text):
        return self.ctx.call("TL", text)


def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/68.0.3440.106 Safari/537.36'}
    req = requests.get(url=url, headers=headers)
    return req.content.decode('utf-8')


def max_length(content):
    if len(content) > 4891:
        raise FunctionValueError('{} 文本长度超过限制'.format(content))


def output_result(parm, prt=False):
    # print(parm)

    str_end = parm.find(",[null,null")
    need_str = parm[2:str_end]

    li_s = need_str.split('],[')
    res = []
    for i in li_s:
        res.append(find_result_content(i))
    com_res = ''.join(res)
    if prt is True:
        print(com_res)
    return com_res


def en_to_zn_translate(content, tk):
    max_length(content)
    content = urllib.parse.quote(content)
    # 英译汉
    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (tk, content)
    result = open_url(url)
    # output_result(result)
    return result


def zn_to_en_translate(content, tk):
    max_length(content)
    content = urllib.parse.quote(content)
    # 汉译英
    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8" \
          "&source=btn&ssel=3&tsel=3&kc=0&tk=%s&q=%s" % (tk, content)
    result = open_url(url)
    output_result(result)


def main():
    import termcolor
    js = ReturnTk()
    while True:
        print(termcolor.colored("请先输入要进行的操作：q表示退出；e表示英文翻译成中文；z表示中文翻译成英文。", "red"))
        change = input("请选择翻译选项：")
        if change == 'q':
            break
        elif change == 'e':
            txt = input("请输入要翻译的英文：")
            tk = js.get_tk(txt)
            en_to_zn_translate(txt, tk)
        elif change == 'z':
            txt = input("请输入要翻译的中文：")
            tk = js.get_tk(txt)
            zn_to_en_translate(txt, tk)
        else:
            print("请输入正确的选项！")


def find_result_content(s):
    """找到第一个匹配的双引号里面的内容"""
    if type(s) is not str:
        raise TypeError('{} is not a string.'.format(s))
    first_quote = s.find('\"')
    s = s[first_quote + 1:]
    second_quote = s.find('\"')
    s = s[:second_quote]
    return s


def cut_input(content, e=4891):
    """每4891个字符翻译一次"""
    length = len(content)
    li = []
    while length >= e:
        tmp = content[:e]
        # print(tmp)
        while content[0] is '.':
            content = content[1:]
        period_ind = tmp.rfind('.')
        if period_ind == -1:
            period_ind = tmp.rfind('!')
        li.append(content[:period_ind + 1])
        content = content[period_ind + 1:]  # 这句话不改变content
        length = len(content)
        # print(length)

    li.append(content)
    return li


def write_file_li(li, filename, title=''):
    """写一个数组到文件中

    :param li       要写入的数组
    :type li        list
    :param filename 写入的文件名
    :type filename  str
    :param title    标题，会写入文件第一行
    :type title     str
    """
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    if title != '':
        f.write(title + '\n')
    for i in li:
        i = str(i)
        li = i.split('\\n')
        for j in li:
            f.write(j+'\n')
        f.write('\n')
    f.close()


if __name__ == "__main__":
    import argparse
    import os
    import sys
    now_path = os.getcwd()
    dir_path = '/'.join(now_path.split('\\')[:-1])
    sys.path.append(dir_path)  # 把这个加入环境变量

    from small_function.read_pdf import read_pdf_real, del_enter
    from small_gram import get_dir, get_name

    txt1 = '''Hi! I'm Byron. I'm from Changchun. where are you from?
    Hi! I'm Alice. I'm from Paris. where are you from?
    Hi! I'm Bill. I'm from LA. where are you from?
    Hi! I'm Cameron. I'm from Ontario. where are you from?
    '''
    # txt2 = del_enter(txt1)

    # js1 = ReturnTk()
    # tk1 = js1.get_tk(txt1)
    # result1 = en_to_zn_translate(txt1, tk1)
    # output_result(result1)

    # ci = cut_input(txt1, 50)
    # for i1 in ci:
    #     print(i1)

    parser = argparse.ArgumentParser(description='Translate English paper to Chinese.')

    parser.add_argument('input', metavar='input', help='The input must be a pdf file or a string.')
    parser.add_argument('--out', '-o', metavar='output_dir', help='Output directory.', default='E:/下载/')
    args = parser.parse_args()

    inp = args.input

    if os.path.exists(inp):  # 先判断是否为文件
        read = read_pdf_real(inp)
        print('文章读取完毕。长度 %s 。' % len(read))
        cut_read = cut_input(read)
        print('文章裁剪完毕。分为了%s段。' % len(cut_read))
        tl = []
        js2 = ReturnTk()
        for i2 in cut_read:
            tk2 = js2.get_tk(i2)
            trans = output_result(en_to_zn_translate(i2, tk2))
            # print(trans)
            # print('\n'*3)
            tl.append(trans)
        # for i3 in tl:
        #     print(i3)

        path2 = 'E:/下载/cvprw15.txt'
        out_dir = args.out
        out_name = get_name(inp)[0]
        out_dir = out_dir+out_name+'.txt'
        # li3 = ['a', 'b', 'c']
        write_file_li(tl, out_dir)
        print('保存完毕。')
    elif isinstance(inp, str):  # 不是文件就按照一段PDF样式的字符串处理输入
        js3 = ReturnTk()
        inp = del_enter(inp)
        tk3 = js3.get_tk(inp)
        trans_res = en_to_zn_translate(inp, tk3)
        output_result(trans_res, True)
    else:
        raise IOError('Input must be a string or file path')
