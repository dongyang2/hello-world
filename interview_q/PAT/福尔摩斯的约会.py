# 垃圾题目，看半天才看懂，表达能力真差

A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
     'W', 'X', 'Y', 'Z']

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']

# A_G = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# A_N = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

dic1 = {
    'A': 'MON',
    'B': 'TUE',
    'C': 'WED',
    'D': 'THU',
    'E': 'FRI',
    'F': 'SAT',
    'G': 'SUN'
}

dic2 = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
    'G': '16',
    'H': '17',
    'I': '18',
    'J': '19',
    'K': '20',
    'L': '21',
    'M': '22',
    'N': '23'
}

code1 = input()[4:]
code2 = input()[4:]
code3 = input()
code4 = input()

week = []
hour = []
for ii, i in enumerate(code1):
    for jj, j in enumerate(code2):
        if i == j:
            if i in dic1:
                week.append(dic1[i])
                code1 = code1[:ii]+code1[ii+1:]
                code2 = code2[:jj]+code2[jj+1:]
            if i in dic2:
                hour.append(dic2[i])
# print(hour)

minute = []
for ii, i in enumerate(code3):
    for jj, j in enumerate(code4):
        if i == j and ii == jj and i in a:
            minute.append(ii)

hour_f = ''
if int(hour[1]) in range(10):
    hour_f = '0'+hour[1]
else:
    hour_f = hour[1]

minute_f = ''
if minute[0] in range(10):
    minute_f = '0'+str(minute[0])
else:
    minute_f = str(minute[0])

# print(a+A)
print(week[0]+' '+hour_f+':'+minute_f)
