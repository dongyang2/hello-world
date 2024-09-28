#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
import os
import time

os.environ['NO_PROXY'] = '127.0.0.1,localhost'
import ollama


def get_ollama_response(content):
    response = ollama.chat(model='qwen2', messages=[{
        'role': 'user',
        'content': content
    }])
    return response['message']['content']


def make_tran_qwen2(srt_path, out_path=None, opt="字幕", num_of_line=5, start_line=1, retry_time=1):
    """clean代表是否对结果进行规则处理[此参数已废弃]"""
    if out_path and os.path.exists(out_path):
        os.remove(out_path)

    if "字幕" in opt:
        with open(srt_path, 'r', encoding="utf-8") as f:
            li = f.readlines()
            i = 1
            text = ""
            last_line_id = 1
            this_start = 1
            start_line_str = f"{start_line}\n"
            if start_line_str in li:
                start = li.index(start_line_str)
            li = li[start:]

            for j, row in enumerate(li):
                if "时间戳" in opt and "-->" in row:
                    row = timestamp_handler(row, 5)
                if row[:-1].isdigit():
                    last_line_id = int(row[:-1])
                if row == str(start_line + i * num_of_line) + "\n" or j == len(li) - 1:
                    if j == len(li) - 1:
                        text += row
                        num_of_line = last_line_id - start_line - (i-1)*num_of_line + 1
                    content = f'{text} 翻译为 中文，翻译结果中不要删除我的时间标识和序号，且翻译结果中将时间标识、序号、标点与我原先文本格式保持一致，也别给我解释，因为我要做字幕，谢谢'
                    print(content)
                    try:
                        result = get_ollama_response(content)
                        print(f"未处理->\n{result}")
                        result = resp_handler_with_id(result, num_of_line, this_start)
                    except Exception as e:
                        print("返回故障。开始重试。\n", str(e))
                        result = retry(content, num_of_line, retry_time)

                    if result is None:
                        result = text
                    print(f"写入结果->\n{result}")
                    if out_path:
                        with open(out_path, "a+", encoding="utf-8") as f1:
                            f1.write(result)
                    i += 1
                    this_start += num_of_line
                    text = ""
                text += row
            print('\n', '-*-' * 5, ' 翻译完毕 ', time.ctime(), '-*-' * 5)
    else:
        with open(srt_path, 'r', encoding="utf-8") as file:
            for row in file.readlines():
                line_srt = row[:-1]  # 去掉\n
                if len(line_srt) > 0:
                    try:
                        print(line_srt)
                        content = f'"{line_srt}" 翻译为 中文，翻译结果和我原先文本格式保持一致，也别给我解释，谢谢'
                        result = get_ollama_response(content)
                        print(result)

                        if out_path:
                            with open(out_path, "a+", encoding="utf-8") as f:
                                f.write(f"{line_srt[0]}\n{line_srt[1]}\n{result}\n\n")
                    except IndexError as _:
                        print('\n', '-*-' * 5, ' 翻译完毕 ', time.ctime(), '-*-' * 5)
                        break
                    except Exception as e:
                        print(str(e))


def resp_handler(s: str, num: int):
    """处理srt文件的返回结果。通用方法。
    案例见main
    """
    colon_li = []
    for i in range(len(s)):
        if s[i] == ":":
            colon_li.append(i)

    i = 0
    lines = ""
    end = 0  # 其实就是下一个line的开始
    for j in range(num):
        if colon_li[i] < 2 or not s[colon_li[i] - 1].isdigit() or not s[colon_li[i] + 1].isdigit():
            i += 1
        ind1 = colon_li[i]
        num = ""
        for c in s[end:ind1 - 2]:
            if c.isdigit():
                num += c

        ind2 = colon_li[i + 3]
        timeline1 = s[ind1 - 2:ind1 + 10]
        timeline2 = s[ind2 - 5:ind2 + 7]
        timeline = timeline1 + " --> " + timeline2

        i += 4
        if i < len(colon_li):
            if colon_li[i] < 2 or not s[colon_li[i] - 1].isdigit() or not s[colon_li[i] + 1].isdigit():
                i += 1
            ind3 = colon_li[i] - 3
            ind4 = 0
            while ind3 > 0:
                if s[ind3].isdigit():
                    ind4 = ind3 - 1
                    while s[ind4].isdigit():
                        ind4 -= 1
                    break
                ind3 -= 1
            resp = s[ind2 + 7:ind4]
            end = ind4
        else:
            resp = s[ind2 + 7:]
        # print(f"j={j},num={num}, resp={resp}")
        laji = ["：", "-", "]", ":"]
        for la in laji:
            if la in resp:
                t1 = resp.find(la)
                t2 = len(resp) if resp.rfind("\n") == -1 else resp.rfind("\n")
                # print(f"num={num}, t1={t1}, t2={t2}")
                if t2 == t1 + 1:
                    t2 = len(resp)
                resp = resp[t1 + 1:t2 + 1]
                break

        lines += num + "\n" + timeline.replace(".", ",") + "\n" + resp.strip() + "\n\n"

    return lines


def get_line_id(s: str, lid: str, start_find_ind=0):
    colon = ""
    ind1 = 0
    colon_ind = 0

    while colon != ":":
        ind1 = s.find(lid, start_find_ind)
        if ind1 == -1:
            break

        count = 2  # 时间戳必定是 两个数字+冒号开头
        i = 0
        for c in s[ind1 + len(lid):]:
            if c != "\n" and c != " " and not c.isdigit() and c != "[":
                break
            if c.isdigit():
                count -= 1
                if count == 0:
                    colon_ind = ind1 + len(lid) + i + 1
                    colon = s[colon_ind]  # 靠这个时间戳断定找到了字幕序号
                    break
            i += 1

        start_find_ind = ind1 + len(lid)

    if ind1 == -1:
        return None, 0
    else:
        return ind1, colon_ind


def resp_handler_with_id(s: str, num: int, start_id: int):
    """处理srt文件的返回结果。因为srt的每一条字幕的序号，其实是已知的。
    案例见main.

    resp_handler() 通用方法其实是通过找时间戳来确定下一条字幕的位置。但本函数使用字幕序号来确定，情况其实会变简单。
    序号（start_id）就两种情况。
    1.序号\n时间戳
    2.序号 时间戳
    """
    lines = ""
    next_ind = None
    next_colon = None
    for j in range(num):
        id_str = str(start_id)
        id_len = len(id_str)

        if next_ind is None:
            num_ind1, ci1 = get_line_id(s, id_str)
        else:
            num_ind1, ci1 = next_ind, next_colon
        num_ind2, ci2 = get_line_id(s[num_ind1 + id_len:], id_str)

        if num_ind2:  # 在有“Translation:”的案例中，第二个序号才是我们想要的
            num_ind1 += num_ind2 + id_len
            ci1 = num_ind1 + id_len + ci2

        timeline1 = s[ci1 - 2:ci1 + 10]
        ind2 = s.find(":", ci1 + 10)  # 标示第2个时间戳的位置
        timeline2 = s[ind2 - 2:ind2 + 10]
        timeline = timeline1 + " --> " + timeline2

        if j == num - 1:
            resp = s[ind2 + 11:]
        else:
            next_id = str(start_id + 1)
            next_ind, next_colon = get_line_id(s, next_id, ind2+11)
            resp = s[ind2 + 11: next_ind]

        laji = ["：", "-", "]", ":"]
        for la in laji:
            if la in resp:
                t1 = resp.find(la)
                t2 = len(resp) if resp.rfind("\n") == -1 else resp.rfind("\n")
                if t2 == t1 + 1:
                    t2 = len(resp)
                resp = resp[t1 + 1:t2 + 1]
                break

        start_id += 1
        lines += id_str + "\n" + timeline.replace(".", ",") + "\n" + resp.strip() + "\n\n"

    return lines


def timestamp_handler(s: str, limit=6):
    """faster-whisper生成的时间线，有时候时间跨度很长，不合理，需要把它缩短"""
    tmpli = s.split(" ")
    start_time, suffix = tmpli[0].split(",")
    end_time = tmpli[2].split(",")[0]
    start_h, start_m, start_s = [int(x) for x in start_time.split(":")]
    end_h, end_m, end_s = [int(x) for x in end_time.split(":")]
    sub_s = (end_h - start_h) * 3600 + (end_m - start_m) * 60 + end_s - start_s

    if sub_s > limit:
        print(f"原有时间线 {s}")
        if end_s - limit >= 0:
            start_s = end_s - limit
            start_m = end_m
            start_h = end_h
        elif end_m - 1 > 0:
            start_m = end_m - 1
            start_s = end_s + 60 - limit
            start_h = end_h
        else:
            start_h = end_h - 1
            start_m = 59
            start_s = end_s + 60 - limit
    return f"{padding(start_h)}:{padding(start_m)}:{padding(start_s)},{suffix}" + " " + tmpli[1] + " " + tmpli[2]


def padding(a):
    """补全一位数到2位数"""
    if len(str(a)) < 2:
        return "0" + str(a)
    else:
        return a


def retry(content, nol, try_time=1):
    result = None
    for i in range(1, try_time):
        try:
            print(f"第{i}次重试")
            result = get_ollama_response(content+"。只给我翻译，且输出请和输入格式保持一致。")
            print(f"未处理->\n{result}")
            result = resp_handler(result, nol)
            break
        except Exception as e:
            print(f"第{i}次重试失败。 \n{e}")
    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Read PDF')

    parser.add_argument('input', help='文件输入')
    parser.add_argument('--out', help='输出文件路径.', default=None)
    parser.add_argument('--clean', help='是否对机器人翻译的输出结果做处理，比如删除它的解释', default=False)
    parser.add_argument('--opt', help='翻译种类', default='字幕且优化时间戳')
    parser.add_argument('--num_of_line', help='当翻译任务是字幕翻译时，此选项才生效。代表每次翻译的字幕条数。', default=5)
    parser.add_argument('--start_line', type=int, help='当翻译任务是字幕翻译时，此选项才生效。代表从哪个序号的字幕（第几条字幕）开始翻译。', default=1)
    args = parser.parse_args()

    inp_path, out_path, clean, opt, nol = args.input, args.out, args.clean, args.opt, args.num_of_line
    start_line = args.start_line

    # inp_path = "E:/Download/1.txt"
    # out_path = "E:/Download/2.txt"
    # clean = True
    print('-*-' * 5, ' start ', time.ctime(), '-*-' * 5, '\n')

    make_tran_qwen2(inp_path, out_path, opt, nol, start_line)


#     s1 = """140
# 00:40:14,790 --> 00:40:21,060 - 翻译结果了"""
#     s2 = "150 00:42:27,480 --> 00:42:30,860 翻译结果？"
#     s3 = """45
# [00:03:24.690, 00:03:25.690] 翻译结果"""
#     s4 = """6 00:00:19,200 --> 00:00:23,400
# 翻译结果"""
#     s5 = """225
#     [01:21:07,060 --> 01:21:11,500]
# 翻译结果"""
#     s6 = """208   01:18:05,270 --> 01:18:35,210 xxx
#
# 翻译：翻译结果。"""
#     s7 = """Translation:
# 163
# 00:46:56,790 --> 00:46:58,790
# 翻译结果"""
#     print(resp_handler(s1))
#     print(resp_handler(s2))
#     print(resp_handler(s3))
#     print(resp_handler(s4))
#     print(resp_handler(s5))
#     print(resp_handler(s6))
#     print(resp_handler(s7))


if __name__ == '__main__':
    main()
