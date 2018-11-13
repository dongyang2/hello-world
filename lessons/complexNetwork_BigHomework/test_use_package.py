#! python3
import networkx


def get_max_bt_edge(g):
    bt = networkx.edge_betweenness(g)  # 获得边的betweenness
    a = 0.0
    b = (0, 0)
    for i1 in bt.items():
        if i1[1] >= a:
            a = i1[1]
            b = i1[0]
    return b


if __name__ == '__main__':
    e = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
    G = networkx.Graph(e)  # 为图G添加边
    # print(networkx.degree_histogram(G))
    networkx.Graph.remove_edge(G,1,2)
    print(G.edges)