#!python 3
# utf-8


def bubble_sort(li):
    """冒泡排序。遍历n次列表，每一次确定第i（1<i<=n）大的数。每一次遍历过程中，最大的数总是会冒泡到最后一个。"""
    n = len(li)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if li[j] >= li[j + 1]:
                tmp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = tmp
    return li


def quick_sort(li, p, r):
    """算法导论 快速排序 递归部分"""
    if p < r:
        q = partition_by_start(li, p, r)
        quick_sort(li, p, q - 1)
        quick_sort(li, q + 1, r)


def partition(li, start, end):
    """算法导论 快速排序 划分部分"""
    i = start - 1
    for j in range(start, end):
        if li[j] <= li[end]:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[end], li[i + 1] = li[i + 1], li[end]
    return i + 1


def partition_up(li, start, end):
    """算法导论 快速排序 划分部分 改版"""
    i = start
    for j in range(start, end):
        if li[j] <= li[end]:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[end], li[i] = li[i], li[end]
    return i


def partition_by_start(li, start, end):
    """把开始元素作为对比元素的划分方法，根据partition改编。得到从大到小的有序结果。
    一开始我想把开始元素做对比元素，然后还是得到从小到大的结果，发现这样会增加操作次数。"""
    i = end+1
    j = end
    while j > start:
        if li[j] < li[start]:
            i -= 1
            li[i], li[j] = li[j], li[i]
        j -= 1
    li[i-1], li[start] = li[start], li[i-1]
    return i-1


def quick_sort_non_recursion(li, start, end):
    stack = [start, end]
    while len(stack) != 0:
        end = stack.pop()
        start = stack.pop()
        p = partition_up(li, start, end)
        if start < p-1:
            stack.append(start)
            stack.append(p-1)
        if p+1 < end:
            stack.append(p+1)
            stack.append(end)


def is_ascend(li):
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True


def heap_sort(li):
    """堆排序。
    思想特别简单，以大根堆为例。
    每次把二叉树里最大的元素移动到根节点，交换根节点与最后一位。
    再从除了最后一位的元素里，找到最大的元素，移动到根节点，交换根节点与倒数第二位。
    ······
    当二叉树只有一个根节点时，排序完成。
    """
    end = len(li)-1
    while end > 0:
        build_heap(li, end)
        li[0], li[end] = li[end], li[0]
        end -= 1


def build_heap(li, end):
    """建立大根堆"""
    parent_tmp = -1
    for i in range(end):
        parent = int((end-i-1)/2)
        if parent != parent_tmp:
            if parent*2+1 < end+1:
                if li[parent*2+1] > li[parent]:
                    li[parent*2+1], li[parent] = li[parent], li[parent*2+1]
            if parent*2+2 < end+1:
                if li[parent*2+2] > li[parent]:
                    li[parent*2+2], li[parent] = li[parent], li[parent*2+2]
            parent_tmp = parent


def main():
    c = [-10, -5, 0, 5, 3, 10, 15, -20, 25]
    # c = [2, 8, 7, 1, 3, 5, 6, 4]
    # c = [-5, -20, 0, 6, 1]
    quick_sort(c, 0, len(c) - 1)
    print(c)


if __name__ == "__main__":
    main()
