# coding: utf-8
# 由于手机玩游戏时，有时候会保存创建日期，但是此时没有拍摄日期，但有时候反之
# 那么就需要读取他们的日期进行排序，要么按拍摄排序，要么按创建日期排序
# 目前不知道出现此情况的原因，可能是miui版本问题导致的截图文件的文件属性不一样，miui自2021年之后我将对其一生黑！

# 后来想了下还是不对，创建日期居然很多图片是一样的，那么思路就变了---- 把相同图片找出来，打印。

from PIL import Image, ImageChops
import time, os

from small_gram.file_op import ergodic_dir


def is_same_pic(pic_path1, pic_path2):

    a = Image.open(pic_path1)
    b = Image.open(pic_path2)
    diff = ImageChops.difference(a, b)

    if diff.getbbox() is None:
        return True
    else:
        return False


def test_print():

    img_path = 'E:/玩忆/原神/1652200656953.jpg'  # 有拍摄日期
    imge = Image.open(img_path)
    exif_data = imge._getexif()
    # print(exif_data)

    # 取拍摄日期
    image_date = exif_data[36867]
    # 或者 image_date = exif_data[306]
    print("拍摄日期", image_date)

    # 取创建日期
    img_path = 'E:/玩忆/原神/1652200656738.png'
    m_time = os.path.getmtime(img_path)
    # print("m time ", m_time)  // 时间戳
    image_date = time.ctime(m_time)

    print("创建日期", image_date)


def check_same():
    di_fi_li = ergodic_dir("E:/玩忆/原神/")
    file_li = []
    for fd in di_fi_li:
        if os.path.isfile(fd) and is_pic(fd):
            file_li.append(fd)
    # print(len(di_fi_li))
    # print(len(file_li))

    file_num = len(file_li)
    for i in range(file_num):
        for j in range(i + 1, file_num):
            if is_same_pic(file_li[i], file_li[j]):
                print(file_li[i], file_li[j])

def is_pic(file_name: str):
    # 简易版的判定图片
    suffix = file_name.split(".")[-1]
    if suffix in ["jpg", "png", "gif"]:
        return True
    else:
        return False


def del_prefix(dir_name: str):
    # 干掉文件名前缀
    prefix = "Screenshot_"
    prefix_len = len(prefix)
    di_fi_li = ergodic_dir(dir_name, False)
    for file in di_fi_li:
        if prefix in file:
            new_name = file[prefix_len:]
            os.rename('%s/%s' % (dir_name, file), '%s/%s' % (dir_name, new_name))


def main():
    # check_same()
    dn = "E:/玩忆/原神/自打剧情保存"
    # del_prefix(dn)
    print()


if __name__ == "__main__":
    main()
