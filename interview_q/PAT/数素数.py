# 本题体会
#     用for i in range(m) 比i=0 while i<m: i+=1 要快

import math
import time

t0 = time.time()

inp_li = input().split(' ')

# t1 = time.time()

pm = int(inp_li[0])
pn = int(inp_li[1])

# t2 = time.time()
# print('--切开--', int(round(t2 * 1000)) - int(round(t1 * 1000)))    # 毫秒级时间戳

strange_li = []
# i = 2
# while i < 100000000000:
for i in range(2, 1000000000000):
    if len(strange_li) == pn:
        break

    not_prim = 0
    # j = 2
    # while j < math.sqrt(i)+1:
    j_end = int(math.sqrt(i))+1
    for j in range(2, j_end):
        if i % j == 0:
            not_prim = 1
            break
        # j += 1
    if not_prim == 0:
        strange_li.append(i)
    # i += 1

# t3 = time.time()
# print('---get primary number---', int(round(t3 * 1000))-int(round(t2 * 1000)))    # 毫秒级时间戳
# print(strange_li)

row = 1
s = ''
# k = pm-1
# while k < pn:
for k in range(pm-1, pn):
    if row % 10 == 0:
        s = s+str(strange_li[k])
        print(s)
        s = ''
    else:
        s = s+str(strange_li[k])+' '

    if k == pn-1:
        print(s[:-1])
    row += 1
    # k += 1

# t4 = time.time()
# print('---end---', int(round(t4 * 1000)) - int(round(t3 * 1000)))    # 毫秒级时间戳
