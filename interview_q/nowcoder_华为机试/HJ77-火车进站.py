import sys
import copy

def into_station(inp_li: list, stack: list, save_li: list, i: int, action: str, tmp_li: list):
    if action == "in":
        if i < len(inp_li):
            stack.append(inp_li[i])
            i += 1
        else:  # 输入队列为空，即都进了栈
            return
    else:  # 出栈
        if stack:
            elem = stack.pop()
            tmp_li.append(elem)
        else:  # 栈空，无法出栈
            if i == len(inp_li):  # 栈空且输入队列为空，程序结束并保存当前结果
                save_li.append(tmp_li)
            return

    into_station(inp_li, copy.deepcopy(stack), save_li, i, "in", copy.deepcopy(tmp_li))
    into_station(inp_li, copy.deepcopy(stack), save_li, i, "out", copy.deepcopy(tmp_li))

n = input()
li = input()
li1 = [x for x in li.split(" ")]
save_li = []
into_station(li1, [], save_li, 0, "in", [])
for elem in sorted(save_li):
    print(" ".join(elem))
    