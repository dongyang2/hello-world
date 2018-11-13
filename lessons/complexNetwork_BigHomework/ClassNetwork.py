import xlrd

from lessons.complexNetwork_BigHomework.graph_need import turn_table_to_adjacency_matrix, internet_attack, random_attack
from lessons.complexNetwork_BigHomework.draw import line_picture

OriginalTableFile = xlrd.open_workbook('write.xls')

NameTable = OriginalTableFile.sheet_by_index(0)
HometownTable = OriginalTableFile.sheet_by_index(1)
DialectTable = OriginalTableFile.sheet_by_index(2)

# name_degree_distribution = degree_distribution(NameTable)
# home_degree_distribution = degree_distribution(HometownTable)
# dialect_degree_distribution = degree_distribution(DialectTable)

# name_clustering_coefficient = cluster_coefficient(NameTable)
# print(node_degree(row1))


name_adj_matrix = turn_table_to_adjacency_matrix(NameTable)
home_adj_matrix = turn_table_to_adjacency_matrix(HometownTable)
dialect_adj_matrix = turn_table_to_adjacency_matrix(DialectTable)

# for num in name_adj_matrix:
#     print(num)
# print(len(NameTable.row_values(0)))
# print(len(name_adj_matrix))

# name_coreness = coreness(name_adj_matrix)
# t_am = t_shortest_path(name_adj_matrix)
#  for num in t_am:
#     print(num)
# print(name_coreness)
# cn_home = coreness(home_adj_matrix)
# print(cn_home)
# cn_dialect = coreness(dialect_adj_matrix)
# print(cn_dialect)

# print('cluster coefficient of name table ', cluster_coefficient_am(name_adj_matrix))
# print('cluster coefficient of home table ', cluster_coefficient_am(home_adj_matrix))
# print('cluster coefficient of dialect table ', cluster_coefficient_am(dialect_adj_matrix))


# apl_name = average_path_length(name_adj_matrix)
# print('Average path length of name table ', apl_name)
# apl_home = average_path_length(home_adj_matrix)
# print('Average path length of home table ', apl_home)
# apl_dialect = average_path_length(dialect_adj_matrix)
# print('Average path length of dialect table ', apl_dialect)

# t1 = get_weight_matrix(name_adj_matrix)
# for num in t1:
#     print(num)
# print(len(t1))

# node_number_of_subgraph(name_adj_matrix)
# ma = node_num_of_max_subgraph(name_adj_matrix)
# print(ma)

# internet_attack(name_adj_matrix)
# random_attack(name_adj_matrix)

ia_dialect = internet_attack(dialect_adj_matrix)
ra_dialect = random_attack(dialect_adj_matrix)
# print(len(ia_name[0]), len(ia_name[1]))
xl = 'Number of deleted node(dialect table)'
line_picture(range(1, 65), ia_dialect[0], xl, 'Node number of maximal connected subgraph')
line_picture(range(1, 65), ia_dialect[1], xl, 'Average path length')
line_picture(range(1, 65), ra_dialect[0], xl, 'Node number of maximal connected subgraph')
line_picture(range(1, 65), ra_dialect[1], xl, 'Average path length')

# dd_name = degree_distribution(name_adj_matrix)
# histogram_picture(dd_name, 'Degree', 'Node number')
# dd_home = degree_distribution(home_adj_matrix)
# histogram_picture(dd_home, 'Degree', 'Node number')
# dd_dialect = degree_distribution(dialect_adj_matrix)
# histogram_picture(dd_dialect, 'Degree', 'Node number')


