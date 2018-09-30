import os
import numpy as np
# from scipy import misc
from PIL import Image


def read_file_bytes(filename):
    """读取文件内容"""
    with open(filename, 'rb') as f_open:
        file_content = []
        # pre = ''
        for each_line in f_open:
            file_content.append(each_line[2:-2])     # 去掉回车符
        return file_content


def get_row_num(filename):
    with open(filename, 'rb') as f_open:
        return len(f_open.readlines())


def each_byte_file_name_info_sec(path):
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        # print(each_path[-1])
        if each_path[-1] == 's':
            di_fi.append(each_path)
    return di_fi


def write_in_image(content, filename):
    arr = []
    ar = []
    h = 1
    for i in content:
        li = str(i)[2:-1].split(' ')        # 将每一行转为元素为字符串的列表
        for j, k in enumerate(li):
            if j == 0:
                str1 = k[:2]
                str2 = k[2:4]
                str3 = k[4:]
                ar.append(int(str1, 16))
                ar.append(int(str2, 16))
                ar.append(int(str3, 16))
            elif k == '??':
                ar.append(0)
            elif k != '':
                # print(h, k)
                ar.append(int(k, 16))
        # print(ar)
        if h == len(content):
            ar = fill_up_list(ar, 950)
            arr.append(ar)
        elif h % 50 == 0:       # 每50行合并为一行
            # print(ar)
            arr.append(ar)
            ar = []
            # break
        h += 1
    # print(np.array(arr).shape)
    im = Image.fromarray(np.array(arr))
    im.save(filename)
    # misc.imsave(filename, np.array(arr))          # 会报错说没这个函数，下面这行也一样
    # misc.toimage(np.array(arr), 255, 0)


def fill_up_list(li, num_len):
    len_li = len(li)
    while len_li < num_len:
        li.append(0)
        len_li += 1
    return li


def write_png(buf, width, height):
    """ buf: must be bytes or a bytearray in Python3.x,
        a regular string in Python2.x."""
    import zlib
    import struct

    # reverse the vertical line order and add null bytes at the start
    width_byte_4 = width * 4
    raw_data = b''.join(b'\x00' + buf[span:span + width_byte_4]
                        for span in range((height - 1) * width_byte_4, -1, - width_byte_4))

    def png_pack(png_tag, data):
        chunk_head = png_tag + data
        return (struct.pack("!I", len(data)) +
                chunk_head +
                struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head)))

    return b''.join([
        b'\x89PNG\r\n\x1a\n',
        png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
        png_pack(b'IDAT', zlib.compress(raw_data, 9)),
        png_pack(b'IEND', b'')])


def get_image_name(path, str1):
    str2 = str1.split('/')[-1][:-5]
    str3 = path + '/' + str2 + 'png'
    return str3


if __name__ == '__main__':
    path1 = "../resource"
    path2 = 'H:/infosec/train'
    path3 = 'H:/infosec/lan'
    each_name = each_byte_file_name_info_sec(path2)
    for q, l in enumerate(each_name):
        # print(read_file(l))
        m = read_file_bytes(l)
        name_i = get_image_name('H:/infosec/train_image', l)
        # print('now write ', name_i)
        if q % 20 == 0:
            print('Now write ', name_i)
        write_in_image(m, name_i)

        # print(name_i)
        # print(m)
        # for n in m:
        #     print(type(n), ' ', len(n), n)      # n是一行
        #     li1 = str(n)[2:-1].split(' ')
        #     for o, p in enumerate(li1):
        #         if o == 0:
        #             s1 = p[:2]
        #             s2 = p[2:4]
        #             s3 = p[4:]
        #             print(o, p, int(s1, 16), int(s2, 16), int(s3, 16))
        #         else:
        #             print(o, p, int(p, 16))
        #     break
        # break

    # model = Sequential()
    # model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
    #                  activation='relu',
    #                  input_shape=input_shape))

    # a = 123
    # print(type(bytes(b'FA')), type(b'FA'), b'123', bytes(int(a)))
