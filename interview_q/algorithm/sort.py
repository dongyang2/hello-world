# python 3
# utf-8


def bubble_sort(li):
    """冒泡排序。遍历n次列表，每一次确定第i（1<i<=n）大的数。每一次遍历过程中，最大的数总是会冒泡到最后一个。"""
    n = len(li)
    for i in range(n-1):
        for j in range(n-i-1):
            if li[j] >= li[j+1]:
                tmp = li[j]
                li[j] = li[j+1]
                li[j+1] = tmp
    return li


def quick_sort(li, p, r):
    """算法导论 快速排序 递归部分"""
    if p < r:
        q = partition(li, p, r)
        quick_sort(li, p, q - 1)
        quick_sort(li, q + 1, r)


def partition(li, start, end):
    """算法导论 快速排序 划分部分"""
    i = start-1
    for j in range(start, end):
        if li[j] <= li[end]:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[end], li[i+1] = li[i+1], li[end]
    return i+1


def partition_by_start(li, start, end):
    """把开始元素作为对比元素的划分方法，根据partition改编"""
    i = start
    for j in range(start+1, end):
        if li[j] <= li[start]:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[start], li[i] = li[i], li[start]
    return i


def main():
    c = [-10, -5, 0, 5, 3, 10, 15, -20, 25]
    # c = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(c, 0, len(c) - 1)
    print(c)

    
if __name__ == "__main__":
    main()
