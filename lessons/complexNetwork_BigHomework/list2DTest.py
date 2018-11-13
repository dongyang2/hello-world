list_2d = [[0 for col in range(63)]for row in range(63)]
list_2d[0][2] = 3
list_2d[0][3] = 2
list_2d[1][2] = 1
list_2d[1][3] = 4
print(list_2d[0])           # 按行的索引号打印
i = 0
while i < 63:               # 按列打印
    # print(list_2d[num][2])
    i = i+1
count = 0
for j in list_2d:
    count = count+1
# print(count)                # 这里遍历list_2d只有63个元素说明每个j是一个一维list,所以就有了第二种按列打印的方法
# for each_c in list_2d:           # 第二种按列打印
#     print(each_c[2])
# list_2d.pop(0)                # 按行的索引号删除
for j in list_2d:
    j.pop(2)
# print(list_2d[0])
# print(list_2d[1])

