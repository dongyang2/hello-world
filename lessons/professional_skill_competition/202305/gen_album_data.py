# coding: utf-8
# Python 3
# 生产数据

import random


def main():
    album_type = ["直板", "曲屏", "刘海", "挖孔", "屏下光学指纹", "侧边指纹", "后置指纹", "屏下超声波指纹", "三维结构光"]

    album_num = 8
    song_num = 30
    path = "F:/wsl_linux/download/phone_data.txt"
    album_id_type_map = dict()
    song_id_album_map = dict()
    # rand_seed = 202305
    # random.seed(rand_seed)

    f = open(path, 'w', encoding='utf-8')
    for i in range(500):
        if i == 0:
            f.write("型号,厂商,手机类型,销量\n")
        else:
            name = "factory" + str(random.randint(1, album_num))
            this_type = album_type[random.randint(0, len(album_type) - 1)]
            # sales = str(random.randint(1, 100))
            song = "phone" + str(random.randint(1, song_num))
            if i % 100 == 0:
                play_num = str(random.randint(2, 20000))
            else:
                play_num = str(random.randint(2, 1000))

            if song in song_id_album_map:
                name = song_id_album_map[song]
            else:
                song_id_album_map[song] = name

            if song in album_id_type_map:
                this_type = album_id_type_map[song]
            else:
                album_id_type_map[song] = this_type

            f.write(",".join([song, name, this_type, play_num]) + '\n')
    print(set(album_id_type_map.values()))
    f.close()


if __name__ == '__main__':
    main()
