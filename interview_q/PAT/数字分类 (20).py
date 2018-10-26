times_sequence = input().split(' ')
inp_li = []
for i in times_sequence[1:]:
    inp_li.append(int(i))

A1 = 0
A2_li = []
A3 = 0
A4_li = []
A5_li = []

for i in inp_li:
    if i % 5 == 0 and i % 2 ==0:
        A1 += i
    elif i % 5 == 1:
        A2_li.append(i)
    elif i % 5 == 2:
        A3 += 1
    elif i % 5 == 3:
        A4_li.append(i)
    elif i % 5 == 4:
        A5_li.append(i)

if A1 == 0:
    A1 = 'N'

if len(A2_li) == 0:
    A2 = 'N'
else:
    A2 = 0
    neg = 1
    for i in A2_li:
        A2 += neg*i
        neg = neg*-1

if A3 == 0:
    A3 = 'N'

if len(A4_li) == 0:
    A4 = 'N'
else:
    A4 = round(sum(A4_li)/len(A4_li)*1.0, 1)

if len(A5_li) == 0:
    A5 = 'N'
else:
    A5 = max(A5_li)

print(A1, A2, A3, A4, A5)


