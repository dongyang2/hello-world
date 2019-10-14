# https://leetcode-cn.com/problems/filling-bookcase-shelves/
# coding:utf-8
# Python 3


def fill_bookcase(li, w):
    ll = len(li)
    if ll == 1:
        return li[0][1]

    min_sum_h = [li[0][1]]
    now_floor_h = [li[0][1]]
    now_floor_w = [li[0][0]]
    all_floor = [[1]]
    for i in range(1, ll):
        tmp_w = sum(now_floor_w)
        if li[i][0] + tmp_w <= w:  # 这一层还能放下，就接着放
            if li[i][1] > min_sum_h[-1]:
                min_sum_h[-1] = li[i][1]
            now_floor_h.append(li[i][1])
            now_floor_w.append(li[i][0])
            all_floor[-1].append(i+1)
        else:  # 不能放的话，就试着1 创建新层；2 把前面的书放到新层试试会不会让总高度变小
            tmp = [li[i][1]]  # 保存新层的书
            new_floor = li[i][1] + sum(min_sum_h)  # 只放li[i]新层的高度
            min_h = new_floor
            jilu_j = 0
            j = 0
            jilu_w = li[i][0]
            while True:
                if -1-j > -len(now_floor_h):
                    jilu_w += now_floor_w[-1-j]
                    if jilu_w >w:
                        break
                    tmp.append(now_floor_h[-1 - j])
                    tt_h = max(tmp) + max(now_floor_h[:-1 - j]) + sum(min_sum_h[:-1])
                else:
                    break

                if tt_h <  min_h:
                    min_h = tt_h
                    jilu_j = j
                j += 1

            if min_h == new_floor:  # 创建新层的总高度最小
                min_sum_h.append(li[i][1])
                now_floor_w = [li[i][0]]
                now_floor_h = [li[i][1]]

                all_floor.append([i+1])
            else:
                min_sum_h[-1] = max(now_floor_h[:-1-jilu_j])
                # all_floor.append()
                last_floor = all_floor[-1][:-1-jilu_j]
                now_floor = all_floor[-1][-1-jilu_j:]+[i+1]
                all_floor[-1] = last_floor
                all_floor.append(now_floor)
                now_floor_w = now_floor_w[-1-jilu_j:]+[li[i][0]]
                now_floor_h = now_floor_h[-1-jilu_j:]+[li[i][1]]
                min_sum_h.append(max(now_floor_h))
    print(all_floor)
    print(min_sum_h)
    return sum(min_sum_h)


def get_height(li):
    """计算当前层高度"""
    h = 0
    for i in li:
        if i[2] > h:
            h = i[2]
    return h


def fill_bookcase_new(li, w):
    """网上的"""
    ll = len(li)
    if ll == 1:
        return li[0][1]

    floor_h = []
    all_floor = []  # 保留各层信息
    ans = [0]+[10000001 for _ in li]  # 网上的和我的最大的不同，记录每一本书的最优解，我总想按层记录
    for i in range(1, ll+1):
        # 试着1 创建新层；2 把前面的书放到新层试试会不会让总高度变小
        tmp = []  # 保存新层的书

        jilu_j = 0
        h = 0
        j = i
        jilu_w = 0
        while j > 0:
            jilu_w += li[j-1][0]
            if jilu_w >w:
                break
            tmp.append(li[j-1][1])

            h = max(h, li[j-1][1])  # 最后一层的高度
            if ans[i] > (ans[j-1] + h):
                ans[i] = ans[j-1] + h
                jilu_j = j
            j -= 1

        if jilu_j == i:
            floor_h.append(tmp)  # 创建新层
            all_floor.append([i])
        else:
            pass

    print(floor_h)
    print(all_floor)
    return ans[-1]


def main():
    # li = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    li =  [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    li = [[2,7],[9,1],[6,1],[4,2],[3,3],[8,6],[10,3],[1,10]]

    print(fill_bookcase_new(li, 10))
    # print(minHeightShelves(li, 10))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
