#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
# 合并讯飞输入法词库。 合并多个user_dict.txt文件


import os


def process_user_dict(input_paths, output_path, gaopinci, encoding='utf-8'):
    """
    处理用户词库文件：合并、去重、清理
    :param input_paths: 输入文件路径列表（多个user_dict.txt）
    :param output_path: 输出文件路径
    :param encoding: 文件编码（默认utf-8，讯飞导出一般为utf-8）
    """
    # 存储去重后的词条（用集合自动去重）
    unique_words = set()
    start_lines = []
    read_start_line = 0

    # 遍历所有输入文件
    for file_path in input_paths:
        if not os.path.exists(file_path):
            print(f"⚠️  文件不存在，跳过：{file_path}")
            continue

        try:
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                lines = f.readlines()

            # 处理每一行：去空行、去首尾空格、去重
            for line in lines:
                if line.startswith("#"):
                    if read_start_line == 0:
                        start_lines.append(line)
                    continue
                # 清理行内容（去掉换行符、首尾空格）
                line0 = line.strip()
                word = line0.split(" ")[0]
                # 跳过空行和纯空格行
                if not line0:
                    continue
                if one_char(word)  or has_123(word) :
                    continue
                unique_words.add(line0)

            print(f"✅  成功处理：{file_path}，提取词条数：{len(lines)}，去重后总词条数：{len(unique_words)}")
            read_start_line += 1

        except Exception as e:
            print(f"❌  处理文件失败：{file_path}，错误：{str(e)}")

    # 无有效词条的情况
    if not unique_words:
        print("⚠️  未提取到任何有效词条！")
        return

    # 将去重后的词条排序（可选，保持有序更易查看）
    sorted_words = sorted(unique_words)
    print(f"去重后 总词条数： {len(sorted_words)}")
    # print(start_lines)
    # sorted_words = start_lines + sorted_words
    for elem in sorted_words:
        print(elem)

    # # 写入输出文件
    # try:
    #     with open(output_path, 'w', encoding=encoding) as f:
    #         # 按讯飞格式，每行一个词条
    #         f.write('\n'.join(sorted_words))
    #     print(f"\n🎉  合并去重完成！")
    #     print(f"📄  输出文件：{output_path}")
    #     print(f"📊  最终有效词条数：{len(sorted_words)}")
    # except Exception as e:
    #     print(f"❌  写入输出文件失败：{str(e)}")


def one_char(line:str):
    """判定 只有一个汉字或者单词的"""
    li = line.split(" ")
    s = li[0]
    # 第一步：字符串长度必须为1
    if len(s) != 1:
        return False
    # 第二步：判断是否为中文字符（Unicode区间）
    return '\u4e00' <= s <= '\u9fff'

def has_123(s:str):
    """去掉 “数字，上，下，不，两，仨，个，也，了，人，斤，会，但，你，我，做，先，再，几，刚”等"""
    t = "一二三四五六七八九十上下不两仨个也了人今会但你我做先再几刚别到前加千百万去又双发只可吃和哦哪呐啊嗯在多大小好就带很怎么儿哇哈太对嘻是的"
    for i in t:
        if i in s:
            return True
    return False

def has_chinese_ge5(s):
    import re
    """
    判断字符串中包含的中文字符数量≥5（允许混其他字符）
    :param s: 待判断字符串
    :return: (是否≥5个中文, 实际中文数量)
    """
    # 正则匹配所有中文字符（基本区+扩展区）
    chinese_pattern = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df\U0002a700-\U0002b73f]')
    # 提取所有中文字符
    chinese_chars = chinese_pattern.findall(s)
    # 统计数量
    chinese_count = len(chinese_chars)
    # 判断是否≥5
    return chinese_count >= 5

def get_gaopinci(file_path):
    li = []
    with open(file_path, 'r', encoding="utf-8", errors='ignore') as f:
        lines = f.readlines()
        for line in lines:
            # print(line.strip().split("\t")[0])
            li.append(line.strip().split("\t")[0])
    # print(li)
    return li

def main():
    g_li = get_gaopinci("E:/备份/输入法导出词库/讯飞输入法/高频词.txt")
    process_user_dict(
        input_paths=[
            'E:/备份/输入法导出词库/讯飞输入法/Neo9-20260207/user_dict.txt',
            'E:/备份/输入法导出词库/讯飞输入法/S23-20260207/user_dict.txt',
            "E:/备份/输入法导出词库/讯飞输入法/Y700-20260207/user_dict.txt"
        ],  # 你的多个词库文件路径
        output_path='merged_user_dict.txt',                # 输出文件路径
        gaopinci=g_li,
        encoding='utf-8'
    )


if __name__ == '__main__':
    main()
