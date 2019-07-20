# 生成纯色的照片。Windows自带画图无法建立大图片。
# pip install mumpy
# pip install matplotlib
# utf-8


def draw(w, h, color, path):
    import numpy as np
    import matplotlib.image as img

    rgb = []
    if color in color_point.keys():
        rgb_value = color_point[color]
    else:
        rgb_value = color.split(',')
    for digit in rgb_value:
        rgb.append(np.full([w, h, 1], digit, dtype=np.uint8))
    pic = np.concatenate(rgb, axis=2)

    img.imsave(path, pic)


color_point = {
    'red': (255, 0, 0),
    'china-red': (230, 0, 0),
    'tomato': (255, 99, 71),
    'pink': (255, 192, 203),
    'purple': (128, 0, 128),
    'violet': (238, 120, 238),
    'blue': (0, 0, 255),
    'sky-blue': (135, 206, 235),
    'dark-blue': (0, 0, 139),
    'green': (0, 255, 0),
    'eye-green': (199, 237, 204),
    'cyan': (0, 255, 255),
    'yellow': (255, 255, 0),
    'gold': (255, 215, 0),
    'orange': (255, 165, 0),
    'chocolate': (210, 105, 30),
    'brown': (165, 42, 42),
    'silver': (192, 192, 192),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}


def main():
    import argparse

    parser = argparse.ArgumentParser(description='生成纯色图片。')
    parser.add_argument('--out', '-o', help='Output directory.', default='E:/下载/')
    # parser.add_argument('--file_name', '-n', help='File name.', default='pic.jpg')
    parser.add_argument('--color', help='You can pick the color in the list. {}\n'
                                        'Or you could specify the color in the format \"255,255,255\".'
                        .format(color_point.keys()), type=str)
    parser.add_argument('--width', '-w', help='Width of picture.', type=int)
    parser.add_argument('--height', '-he', help='Height of picture.', type=int)
    parser.add_argument('--suffix', '-s', help='Suffix of file.', type=str, choices=['jpg', 'png'], default='jpg')

    args = parser.parse_args()

    height = args.height
    width = args.width
    file_name = '{}{}_w{}_h{}.{}'.format(args.out, args.color, args.width, args.height, args.suffix)
    color = args.color
    draw(height, width, color, file_name)


if __name__ == "__main__":
    main()
