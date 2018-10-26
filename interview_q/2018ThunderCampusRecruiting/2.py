inpu = input()
a, b = inpu.split(' ')
a = int(a)
b = int(b)
if a > b:
    a = b


def find_combine(n, m):
    if n < 1 or m < 1:
        return 0
    result = 0
    if n == m:
        result += 1

    result += find_combine(n-1, m-n)
    result += find_combine(n-1, m)
    return result


print(find_combine(a, b))
