import random


def turn_table_to_adjacency_matrix(t):
    lent = len(t.row_values(0))
    l_2d = [[0 for lum in range(lent-1)]for row in range(lent-1)]
    i = 1
    while i < lent:
        row = t.row_values(i)[1:]
        # print(len(row))
        k = 0
        for j in row:
            # print(k)
            if j == 'y':
                l_2d[i-1][k] = 1
            k = k+1
        i = i+1
    return l_2d


# 这是之前没做table转adj_matrix时用的函数，可以看出，没有邻接矩阵写起来方便，并且后面需要算coreness，最短路径之类的，这个也不方便
# def node_degree(l):
#     count = 0
#     for i in l:
#         if i == 'y':
#             count = count+1
#     return count
#
#
# def list_node_degree(t):              # 返回的那个list是从0开始的，也就是说，list[0]代表第一个点,list[62]代表最后一个
#     i = 1
#     list_degree = []
#     while i < 64:
#         row = t.row_values(i)
#         list_degree.append(node_degree(row))
#         i = i + 1
#     return list_degree


# def cluster_coefficient(t):
#     lnd = list_node_degree(t)
#     i = 1
#     # print(len(lnd))
#     all_cluster_coefficient = 0
#     while i < 64:
#         sums = 0
#         row = t.row_values(i)[1:]
#         k = 0
#         for j in row:
#             if j == 'y':
#                 sums = sums+lnd[k]
#             k = k+1
#         if node_degree(row):
#             i_cl_co = 2*sums/node_degree(row)*(node_degree(row)-1)
#         else:
#             i_cl_co = 0
#         all_cluster_coefficient = all_cluster_coefficient+i_cl_co
#         i = i+1
#     last_cluster_coefficient = all_cluster_coefficient/63
#     return last_cluster_coefficient


def node_degree_am(row):
    count = 0
    for i in row:
        count = count+i
    return count


def list_node_degree_am(t_am):
    i = 0
    list_degree = []
    while i < len(t_am):
        list_degree.append(node_degree_am(t_am[i]))
        i = i+1
    return list_degree


def degree_distribution(t):
    lnd = list_node_degree_am(t)         # lnd的下标对应每个点，lnd的值是每个点的度
    max_d = 0
    arr = []                          # arr是用来存度分布的数组，下标对应度，值对应那个度有多少个点
    for i in lnd:                     # 找到最大的度，存入max_d
        if i >= max_d:
            max_d = i
    i = 0
    while i < max_d+1:
        arr.append(0)
        i = i+1
    # print(max_d, arr, '', len(arr), 'oh')
    i = 0
    while i < max_d+1:
        j = 0
        while j < len(lnd):
            if lnd[j] == i:
                arr[i] = arr[i]+1
            j = j+1
        i = i+1
    return arr


def cluster_coefficient_am(t_am):
    lnd = list_node_degree_am(t_am)
    lent = len(t_am)
    i = 0
    # print(len(lnd))
    all_cluster_coefficient = 0
    while i < lent:
        sums = 0
        row = t_am[i]
        k = 0
        for j in row:
            if j == 1:
                sums = sums+lnd[k]
            k = k+1
        if node_degree_am(row):
            i_cl_co = 2*sums/node_degree_am(row)*(node_degree_am(row)-1)
        else:
            i_cl_co = 0
        all_cluster_coefficient = all_cluster_coefficient+i_cl_co
        i = i+1
    last_cluster_coefficient = all_cluster_coefficient/lent
    return last_cluster_coefficient


def find_node_min_degree(lnd):
    i = 0
    md = 0
    while i < len(lnd):
        if lnd[i] <= lnd[md]:
            md = i
        i = i+1
    return md


def coreness(t):
    cn = 0
    m = 0
    t1 = [[0 for c in range(63)]for r in range(63)]
    for i in t:                         # 复制一个t，避免对原有的t造成影响
        t1[m] = i[:]                    # 这行是复制list的关键代码
        m = m+1
    m = 0
    len_t = len(t1)
    while m < len_t:
        lnd = list_node_degree_am(t1)
        # print(lnd)
        md = find_node_min_degree(lnd)
        t1.pop(md)                       # 剔除度最小的那些点，把他们的行删除
        for i in t1:                     # 剔除度最小的那些点，把他们的列也删除
            i.pop(md)
        if lnd[md] >= cn:
            cn = lnd[md]
        m = m+1
        # print(t[0])
    return cn


def t_shortest_path(t_am):
    t1 = get_weight_matrix(t_am)
    len_t = len(t1)
    # print(t_am)
    # k = 0
    # t1 = [[0 for c in range(63)] for r in range(63)]
    # for i in t_am:
    #     t1[k] = i[:]
    #     k = k + 1
    # i = 0
    # while i < 63:
    #     j = 0
    #     while j < 63:
    #         if t1[i][j] == 0:
    #             t1[i][j] = 999
    #         j = j+1
    #     # print(t_am[i])
    #     i = i+1
    k = 0
    while k < len_t:
        i = 0
        while i < len_t:
            j = 0
            while j < len_t:
                if t1[i][j] > t1[i][k]+t1[k][j]:
                    t1[i][j] = t1[i][k]+t1[k][j]
                j = j+1
            i = i+1
        k = k+1
    return t1


def average_path_length(t_am):
    tsp = t_shortest_path(t_am)
    sums = 0
    len_t = len(t_am)
    i = 0
    while i < len_t:
        j = 0
        while j < len_t:
            if tsp[i][j] != 999:   # 我这里之前设置了一个if等于999就continue，结果发现程序死循环了，看来我还是不太会用continue
                sums = sums+tsp[i][j]
                # print(tsp[i][j])
            j = j+1
            # print(tsp[i][j])
        i = i+1
        # print(sums)
    if len_t < 2:
        apl = 0.0
    else:
        apl = 2*sums/(len_t*(len_t-1))
    return apl


def remove_node(t_am, i):
    t_am.pop(i)
    for j in t_am:
        j.pop(i)
    return


def get_weight_matrix(t_am):
    t1 = get_matrix_copy(t_am)
    i = 0
    len_t = len(t1)
    while i < len_t:
        j = 0
        while j < len_t:
            if t1[i][j] == 0:
                t1[i][j] = 999
            j = j + 1
        # print(t_am[i])
        i = i + 1
    return t1


def get_matrix_copy(t_am):
    k = 0
    t1 = [[0 for c in range(len(t_am))] for r in range(len(t_am))]
    for i in t_am:
        t1[k] = i[:]
        k = k + 1
    return t1


def finish_go_through(arr):  # 判断arr中的所有元素是否都变成了非0数，是则返回1，否则返回0
    f = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            f = 0
            break
        else:
            f = 1
        i = i+1
    return f


def node_number_of_subgraph(t_am):
    i = 0
    k = 1                               # k代表着不同子图的序号
    twm = t_shortest_path(t_am)
    # print(twm)
    len1 = len(twm)
    a = [0 for r in range(len1)]
    f = 0                               # f代表着是否遍历完所有的点，是则等于1，否则等于0
    while f == 0:
        j = 0
        while j < len(a):
            # print('aho.')
            if a[j] == 0:
                i = j
                break
            j = j+1
        len2 = len(twm[i])
        a[i] = k
        j = 0
        while j < len2:
            if twm[i][j] != 999 and j != i:
                a[j] = k
                # print(twm[i][j])
            j = j+1
        k = k+1
        f = finish_go_through(a)
        # print(a)
    # print(a)
    b = [0 for r in range(k-1)]         # 下标代表不同的子图，相应的值代表子图的节点数
    j = 0
    while j < len(a):
        i = 0
        while i < len(b):
            if a[j] == i+1:
                b[i] = b[i]+1
            i = i+1
        j = j+1
    # print(b)
    return a, b, k-1                      # a下标代表着节点，值代表该节点的子图，b下标代表子图，值代表节点数，k-1代表子图数


def node_num_of_max_subgraph(t_am):
    b = node_number_of_subgraph(t_am)[1]
    max_num = 0
    for i in b:
        if i > max_num:
            max_num = i
    return max_num


def internet_attack(t_am):
    li_nns = []
    li_apl = []
    t = get_matrix_copy(t_am)
    num = len(t)
    # k = 0
    while num > 1:
        lnd = list_node_degree_am(t)
        max_i = 0
        j = 0
        for i in lnd:
            if i >= lnd[max_i]:
                max_i = j
            j = j+1
        remove_node(t, max_i)
        nns = node_num_of_max_subgraph(t)
        apl = average_path_length(t)
        li_nns.append(nns)
        li_apl.append(apl)
        # print('最大连通子图的节点数=', nns, '平均最短路径=', apl)
        # print('最大连通子图的节点数=', nns, '平均最短路径=', apl, k)
        # k = k+1
        num = len(t)
    li_nns.append(1)
    li_nns.append(0)
    li_apl.append(0.0)
    li_apl.append(0.0)
    # print('最大连通子图的节点数= 1 平均最短路径= 0.0')                # 现在只剩1个节点
    # print('最大连通子图的节点数= 0 平均最短路径= 0.0')                # 现在没有节点
    return li_nns, li_apl


def random_attack(t_am):
    li_nns = []
    li_apl = []
    t = get_matrix_copy(t_am)
    num = len(t)
    while num > 1:
        ri = random.randint(0, num-1)
        remove_node(t, ri)
        nns = node_num_of_max_subgraph(t)
        apl = average_path_length(t)
        li_nns.append(nns)
        li_apl.append(apl)
        # print('最大连通子图的节点数=', nns, '平均最短路径=', apl)
        num = len(t)
    li_nns.append(1)
    li_nns.append(0)
    li_apl.append(0.0)
    li_apl.append(0.0)
    # print('最大连通子图的节点数= 1 平均最短路径= 0.0')
    # print('最大连通子图的节点数= 0 平均最短路径= 0.0')
    return li_nns, li_apl


# print(random.randint(0, 1))

