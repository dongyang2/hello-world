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


def quik_sort(li, p, r):
    if p < r:
        q = partition(li, p, r)
        quik_sort(li, p, q-1)
        quik_sort(li, q+1, r)


def partition(li, p, r):
    x = li[r]
    i = p-1
    for j in range(p, r-1):
        if li[j] <= x:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[r], li[i+1] = li[i+1], li[r]
    return i+1



def main():
    c = [-10, -5, 0, 5, 3, 10, 15, -20, 25]
    quik_sort(c, 0, len(c)-1)
    print(c)

    
if __name__ == "__main__":
    main()