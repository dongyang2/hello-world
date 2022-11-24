import sys

def sort_abc(inp_s:str, lower_li, upper_li):
    abc_li = []
    symbol_li = ["default" for _ in range(len(inp_s))]
    for i in range(len(inp_s)):
        if inp_s[i] in lower_li or inp_s[i] in upper_li:
            abc_li.append(inp_s[i])
        else:
            symbol_li[i] = inp_s[i]
    # print(symbol_li)

    sorted_abc_li = []
    for i in range(26):
        for j in range(len(abc_li)):
            if abc_li[j] == lower_li[i] or abc_li[j] == upper_li[i]:
                sorted_abc_li.append(abc_li[j])
    # print(sorted_abc_li)

    j = 0
    for i in range(len(symbol_li)):
        if symbol_li[i] == "default":
            symbol_li[i] = sorted_abc_li[j]
            j +=1

    print("".join(symbol_li))


lower_li='abcdefghijklmnopqrstuvwxyz'
upper_li =lower_li.upper()

s = input()
sort_abc(s,lower_li,upper_li)
