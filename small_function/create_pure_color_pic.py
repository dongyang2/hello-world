def draw(w, h, color, path):
    import numpy as np
    import matplotlib.image as img

    rgb = []
    for digit in color_point[color]:
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
    parser.add_argument('--file_name', '-n', help='File name.', default='pic.jpg')
    parser.add_argument('--color', help='Color you pick.', choices=color_point.keys())
    parser.add_argument('--width', '-w', help='Width of picture.', type=int)
    parser.add_argument('--height', '-he', help='Height of picture.', type=int)

    args = parser.parse_args()

    height = args.height
    width = args.width
    file_name = args.file_name
    out_dir = args.out
    color = args.color
    draw(height, width, color, out_dir + file_name)


if __name__ == "__main__":
    main()
