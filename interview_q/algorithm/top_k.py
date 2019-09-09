# Python 3
# coding: utf-8


def top_k_bubble_sort(arr, k):
    # 最小的k个数，冒k个泡
    ll = len(arr)
    for i in range(k):
        for j in range(i+1, ll):
            if arr[j] <= arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[:k]


def main():
    li = [15, 54, 26, 93, 17, 77, 31, 44, 55, 20]

    print(top_k_bubble_sort(li, 5))


if __name__ == '__main__':
    main()
