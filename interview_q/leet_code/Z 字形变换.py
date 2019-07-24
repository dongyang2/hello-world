# https://leetcode-cn.com/problems/zigzag-conversion/
# utf-8
# python3


def zigzag(s: str, numRows: int):
    len_s = len(s)
    if len_s == 0:
        return ''
        # raise ValueError('请输入非空字符串')
    if numRows==1 or len_s==1:
        return s
    if numRows == 2:
        return s[::2]+s[1::2]
    tmp_li = []
    s_index = 0
    cols = get_num_col(len_s, numRows)
    for col in range(cols):
        row_tmp = []
        space = col % (numRows - 1)
        if space == 0:
            for word in range(numRows):
                row_tmp.append(s[s_index])
                s_index += 1
                if s_index == len_s:
                    row_tmp += [' ' for _ in range(numRows-word-1)]
                    break
            tmp_li.append(row_tmp)
        else:
            for _ in range(numRows):
                row_tmp.append(' ')
            row_tmp[numRows-space-1] = s[s_index]
            s_index += 1
            tmp_li.append(row_tmp)

    # print(tmp_li)
    # 转置后按行连接字符
    tmp_s = ''
    for row in range(numRows):
        for col in range(cols):
            now_s = tmp_li[col][row]
            if now_s != ' ':
                tmp_s += now_s
    return tmp_s


def get_num_col(len_s: int, num_row: int):
    count = 0
    row_ = False
    while len_s > 0:
        if row_ is False:
            len_s = len_s - num_row
            count += 1
            row_ = True
        else:
            j = 0
            while j < num_row - 2:
                len_s -= 1
                count += 1
                if len_s == 0:
                    break
                j += 1
            row_ = False
    return count


def main():
    s = 'PAYPALISHIRING'
    print(zigzag(s, 4))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    main()

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
