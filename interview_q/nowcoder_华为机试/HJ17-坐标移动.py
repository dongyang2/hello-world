# coding: utf-8
# Python 3
#
#


def valid_pre(s: str):
    if s.startswith("A") or s.startswith("W") or s.startswith("S") or s.startswith("D"):
        return True
    else:
        return False


def valid_post(s: str, vl: list):
    if s in vl:
        return True
    else:
        return False


def main():
    s1 = input()
    li1 = s1.split(";")
    tmp = [str(x) for x in range(100)]
    x = 0
    y = 0
    for elem in li1:
        if 1 < len(elem) < 4 and valid_pre(elem):
            move = elem[0]
            num = elem[1:]
            if valid_post(num, tmp):
                step = int(num)

                if move == "A":
                    x -= step
                elif move == "D":
                    x += step
                elif move == "W":
                    y += step
                else:
                    y -= step
    print(f"{x},{y}")


if __name__ == '__main__':
    main()
