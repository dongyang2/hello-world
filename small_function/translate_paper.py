# pip install PyExecJS
# pip install bs4

import urllib.parse
import execjs
import requests


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
        print("翻译文本超过限制！")
        return


def output_result(parm):
    str_end = parm.find("]],")
    need_str = parm[2:str_end]

    li_s = need_str.split('],[')[:-1]
    res = []
    for i in li_s:
        res.append(find_result_content(i))
    # print(''.join(res))
    return ''.join(res)


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
    import os
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


def get_dir(fil_nam):
    """获得文件的整个目录，即剔除了文件自己的名字"""
    s = fil_nam.split('/')[:-1]
    tmp_s = ''
    for i in s:
        tmp_s += i + '/'
    return tmp_s


if __name__ == "__main__":
    from small_function.read_pdf import read_pdf_real

    # js1 = ReturnTk()

    txt1 = '''Hi! I'm Byron. I'm from Changchun. where are you from?
    Hi! I'm Byron. I'm from Changchun. where are you from?
    Hi! I'm Byron. I'm from Changchun. where are you from?
    Hi! I'm Byron. I'm from Changchun. where are you from?
    '''
    # txt2 = del_enter(txt1)

    # tk1 = js1.get_tk(txt2)
    # result1 = en_to_zn_translate(txt2, tk1)
    # output_result(result1)

    # ci = cut_input(txt1, 50)
    # for i1 in ci:
    #     print(i1)

    path1 = 'E:/下载/cvprw15.pdf'
    read = read_pdf_real(path1)
    cut_read = cut_input(read)
    tl = []
    js2 = ReturnTk()
    for i2 in cut_read:
        tk2 = js2.get_tk(i2)
        trans = output_result(en_to_zn_translate(i2, tk2))
        tl.append(trans)
    # for i3 in tl:
    #     print(i3)

    path2 = 'E:/下载/cvprw15.txt'
    # li3 = ['a', 'b', 'c']
    write_file_li(tl, path2)
