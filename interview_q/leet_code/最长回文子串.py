# https://leetcode-cn.com/problems/longest-palindromic-substring/
# utf-8
# python3


def find_palindrome(s: str):
    """找到所有回文串"""
    len_s = len(s)
    tmp_li = []
    for i in range(len_s):
        if i < len_s / 2:
            for j in range(i + 1, len_s - i):
                tmp_s = s[i:j + 1]
                if is_pal(tmp_s):
                    tmp_li.append(tmp_s)
        else:
            for j in range(i + 1, len_s):
                tmp_s = s[i:j + 1]
                if is_pal(tmp_s):
                    tmp_li.append(tmp_s)
    return tmp_li


def longest_palindrome(s: str):
    """找到最大回文串

    注意：
    为空字符时返回空字符。
    单字符算回文串。
    """
    len_s = len(s)
    if len_s == 0 or len_s == 1:
        return s
    longest_s = ''
    for i in range(len_s):
        for j in range(i + 1, len_s):
            tmp_s = s[i:j + 1]
            if is_pal(tmp_s) and len(tmp_s) >= len(longest_s):
                longest_s = tmp_s
    if longest_s == '':
        return s[0]
    return longest_s


def is_pal(s: str):
    """判断是否是回文字符串，其实这个不太好。见“回文数.py”文件"""
    len_s = len(s)
    mid = int((len_s + 1) / 2)
    if len_s % 2 == 1:
        return s[:mid - 1] == reverse(s[mid:])
    else:
        return s[:mid] == reverse(s[mid:])


def reverse(s: str):
    tmp_s = ''
    for s_i in s[::-1]:
        tmp_s += s_i
    return tmp_s


def Manacher(s: str):
    """找到最大回文串，这个算法专门用来找最长回文串······"""
    len_s = len(s)
    if len_s == 0 or len_s == 1:
        return s
    padding = '#' + '#'.join([x for x in s]) + '#'
    max_len = len(padding)
    tmp_li = []
    for i in range(max_len):
        count = 0
        while i - count != 0 and i + count != max_len:
            if padding[i - count] == padding[i + count]:
                count += 1
            else:
                break
        tmp_li.append(count)
    longest_pal_len = max(tmp_li)
    index_longest_pal_len = tmp_li.index(longest_pal_len)
    return ''.join(padding[index_longest_pal_len-longest_pal_len+1: index_longest_pal_len+longest_pal_len].split('#'))


def main():
    s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusn" \
        "gkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosom" \
        "fbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnw" \
        "pxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqj" \
        "fivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeo" \
        "aldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhc" \
        "ggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiyw" \
        "pqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzz" \
        "monftqkcudlzfzutplbycejmkpxcygsafzkgudy"
    print(Manacher(s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    main()

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
