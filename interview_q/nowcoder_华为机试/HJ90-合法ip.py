# coding: utf-8
# Python 3


def check_valid(line: str, num_li: list):
    li = line.split(".")
    if len(li) != 4:
        return False
    for elem in li:
        if elem.startswith("0") and len(elem) != 1:
            return False
        for i in elem:
            if i not in num_li:
                return False
        try:
            ip_num = int(elem)
            if 0 <= ip_num < 256:
                continue
            else:
                return False
        except:
            return False
    return True


def main():
    line = input()
    li = [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    if check_valid(line, li):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
