# 鬼谷八荒。灵果计算，最终以到达984为准。
# 贪心回溯法


thr_dic = [50, 151, 352, 623, 984]


def cal_sum(li):
    """计算当前各灵果得到的属性"""
    j = 1
    a = 0
    for i in li:
        a += i * j
        j += 1
    return a


def check_li(li):
    for i in range(len(li)):
        if li[i] < 0:
            return False
        if cal_sum(li[:i+1]) > thr_dic[i]:
            return False

    return True


def ergodic2(target, attr, li, xia, shang, f, mem):
    """回溯法。第二版"""
    mem.append(li)
    f += 1
    an = attr + cal_sum(li)  # 当前结果
    cut = an - target

    if not check_li(li) or f > 30:
        # print("无法达到预期目标")
        return

    if cut == 0:
        return li

    for i in reversed(range(xia, shang)):  # 从后往前搜，速度可能会快，因为an每次变化更大，再进行小值微调。
        add = li[:i] + [li[i] - 1] + li[i + 1:]
        sub = li[:i] + [li[i] + 1] + li[i + 1:]
        if add not in mem:
            tl1 = ergodic2(target, attr, add, i, shang, f, mem)
            if tl1:
                return tl1
        if sub not in mem:
            tl2 = ergodic2(target, attr, sub, i, shang, f, mem)
            if tl2:
                return tl2


def main():
    import argparse
    parser = argparse.ArgumentParser(description='鬼谷八荒。灵果计算。')

    parser.add_argument('attr', metavar='attr', help='初始属性值，默认是1。',type=int, default=1)
    parser.add_argument('--target', metavar='target', help='目标属性值，默认984',type=int, default=984)
    args = parser.parse_args()

    attr = args.attr
    target = args.target

    # 最终能到984的参考各级target —— 984、619、347、149、49
    # target = 984
    # attr = 151  # 当前属性
    # thr_dic = {0: 50, 1: 150, 2: 350, 3: 620, 4: 980}


    li1 = [0 for _ in range(5)]  # 存储最终需要灵果数
    print(li1)

    if target > 984:
        print("到不了这个数，请检查。")
        return

    # 对可用灵果进行定调，如果初始attr较高，肯定不能用低品灵果
    if attr > 979 or attr < 1:
        print("初始属性值不正确，请检查输入。")
        return
    if attr > 620:
        print("当前输入的初始属性已没有操作空间，请检查输入。")
        return
    level = 0  # 这个i是灵果档位， 确定灵果品质下界
    tmp_d1 = [0] + thr_dic
    while level < 4:
        if tmp_d1[level] <= attr < tmp_d1[level + 1]:
            break
        level += 1

    # 先进行初始化，把 最大的可能序列 放进li1
    i = 4
    while i > 0:
        if thr_dic[i - 1] < target <= thr_dic[i]:
            j = i
            cut = target - thr_dic[j - 1]
            while j > level - 1:
                li1[j] = int(cut / (j + 1)) + 1
                if j > level + 1:
                    cut = target - cal_sum(li1) - thr_dic[j - 2]
                elif j == level + 1:
                    cut = target - cal_sum(li1) - attr
                j -= 1
            break
        i -= 1
    print("最大可能 ", li1)

    up = 5  # 确定灵果品质上界
    while up > 0:
        if li1[up - 1] != 0:
            break
        up -= 1

    li2 = ergodic2(target, attr, li1, level, up, 0, [])
    print("回溯结果 - ", li2)
    # # print("回溯结果 sum - ", cal_sum(li2))
    print(",".join([f"需要 {5 - i}品灵果 {li2[i]}个" for i in range(len(li2))]))

    # print(list(range(1,3)))
    # for i in reversed(range(1,3)):
    #     print(i)


if __name__ == '__main__':
    main()
