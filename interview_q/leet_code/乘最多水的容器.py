# https://leetcode-cn.com/problems/container-with-most-water/
# utf-8
# python3


def container(height: list):
    ll = len(height)
    if ll < 2:
        raise ValueError('The input list length must bigger than 2.')
    return not_dp_water(height)


def not_dp_water(li):
    # leetcode双指针法，每次移动较短长度的指针，只遍历一次。
    max_area = 0
    ll = len(li)
    start_point = 0
    end_point = ll-1
    while start_point != end_point:
        now_area = cal_area(li, start_point, end_point)
        if now_area > max_area:
            max_area = now_area
        if li[start_point] < li[end_point]:
            start_point += 1
        else:
            end_point -= 1
    return max_area


def cal_area(li, start_point, end_point):
    h = min(li[start_point], li[end_point])
    w = end_point-start_point
    return h*w


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(container(height))


if __name__ == '__main__':
    import time
    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
