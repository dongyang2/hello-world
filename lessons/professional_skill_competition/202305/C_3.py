# coding: utf-8
# Python 3
# 生产词云


import pandas as pd
import wordcloud


def main():
    path = "F:/wsl_linux/download/phone_data.txt"
    data = pd.read_csv(path, ",", encoding="utf-8")
    # print(data)

    # 统计单品热度
    all_sales = dict()
    for _, elem in data.iterrows():
        song_name = elem[0]
        song_play_num = elem[3]
        # print(song_name, song_play_num)

        if song_name in all_sales:
            all_sales[song_name] += song_play_num
        else:
            all_sales[song_name] = song_play_num
    # print(len(all_sales))

    wc = wordcloud.WordCloud(width=1000, height=800)
    # 如果出现 ValueError: Only supported for TrueType fonts ,升级Pillow版本即可。
    # 报错版本为Pillow 9.0.1，升级至 Pillow-9.5.0 则无报错。
    # 报错原因可能是libfreetype的支持有问题，参考链接（https://stackoverflow.com/questions/76129498/wordcloud-only-supported-for-truetype-fonts）
    wc.generate_from_frequencies(all_sales)
    wc.to_file("F:/wsl_linux/download/wordCloud.png")


if __name__ == '__main__':
    main()
