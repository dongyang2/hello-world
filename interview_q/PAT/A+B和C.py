times = int(input())
for i in range(1, times+1):
    a = input().split(' ')
    b = int(a[0])+int(a[1])
    c = int(a[2])
    # print(b, c)
    if b > c:
        print('Case #%d: true' % i)
    else:
        print('Case #%d: false' % i)
