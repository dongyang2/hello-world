import sys


#
def common_sub(s1: str, s2: str):
    l1 = len(s1)
    l2 = len(s2)
    i = 0
    j = 0
    save_li = []
    tmps = ''
    while i < l1:
        for j in range(l2):
            if s2[j] == s1[i]:
                k = i  # 利用新的指针去匹配，防止多次前缀匹配的情况
                m = j
                while k < l1 and m < l2:
                    if s1[k] == s2[m]:
                        tmps += s2[m]
                    else:
                        if tmps not in save_li:
                            save_li.append(tmps)
                        tmps = ''
                        break
                    k += 1
                    m += 1
                else:
                    if tmps not in save_li:
                        save_li.append(tmps)
                    tmps = ''
        i += 1
    print(save_li)


# 优化了save_li的空间，因为不需要存储最长子串只需要长度，所以可以把save_li的空间省下来
def common_sub_less_room(s1: str, s2: str):
    l1 = len(s1)
    l2 = len(s2)
    i = 0
    tmps = ''
    max_len = 0
    while i < l1:
        for j in range(l2):
            if s2[j] == s1[i]:
                k = i  # 利用新的指针去匹配，防止多次前缀匹配的情况
                m = j
                while k < l1 and m < l2:
                    if s1[k] == s2[m]:
                        tmps += s2[m]
                    else:
                        if len(tmps) > max_len:
                            max_len = len(tmps)
                        tmps = ''
                        break
                    k += 1
                    m += 1
                else:
                    if len(tmps) > max_len:
                        max_len = len(tmps)
                    tmps = ''
        i += 1
    print(max_len)


# 在common_sub_less_room基础上优化了时间，当剩余长度小于max_len时，直接跳过
def common_sub_less_room_less_time(s1: str, s2: str):
    l1 = len(s1)
    l2 = len(s2)
    i = 0
    tmps = ''
    max_len = 0
    while i < l1:
        if l1-i < max_len:
            break
        for j in range(l2):
            if l2-j < max_len:
                break
            if s2[j] == s1[i]:
                k = i  # 利用新的指针去匹配，防止多次前缀匹配的情况
                m = j
                while k < l1 and m < l2:
                    if s1[k] == s2[m]:
                        tmps += s2[m]
                    else:
                        if len(tmps) > max_len:
                            max_len = len(tmps)
                        tmps = ''
                        break
                    k += 1
                    m += 1
                else:
                    if len(tmps) > max_len:
                        max_len = len(tmps)
                    tmps = ''
        i += 1
    print(max_len)


s1 = input()
s2 = input()
common_sub_less_room_less_time(s1, s2)