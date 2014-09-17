#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import networkx as nx
from utils import print_and_exit
import mynx


def main():
    pass


if __name__ == '__main__':
    main()

# {\bf G} ( {\bf V}, {\bf E} )
# {\bf V} = \{ v_1, v_2, ..., v_i \}
# {\bf E} = \{ (v_1, v_2), (v_2, v_3), (v_2, v_6), ..., (v_i, v_j) \}
E = [(1, 2), (2, 3), (2, 6), (3, 4), (4, 5), (4, 6), (6, 7)]
G = mynx.Graph(E, entrance=False)
G.add_node(1, entrance=True)
G.add_node(5, entrance=True)
G.add_node(7, entrance=True)

print('''
  [1--2--3
      |  |
      6--4--5]
      |
      7]
''')

# add path attributes
entrances = {v for v in nx.get_node_attributes(G, 'entrance')}
start_and_goals = itertools.combinations(entrances, 2)
for src, tgt in start_and_goals:
    for p in nx.all_simple_paths(G, src, tgt):
        G.add_path(p)


# b(i,j,k)= \begin{cases}
#   1 & ( v_i , v_j ) \in p_k \\
#   0 & otherwise
# \end{cases}
def ispartof(edge: tuple, path: mynx.Graph.Path) -> bool:
    for i, j in zip(path.data[::1], path.data[1::1]):
        if set(edge) == {i, j}:
            return True
    else:
        return False


# \forall(v_i, v_j) \in {\bf E};
# \tau_{ij}=\sum_{k=1}^{|P|}b(i,j,k)\theta_k
def edge_flow(g: mynx.Graph, e: tuple) -> int:
    tau = 0
    for q in g.paths:
        if ispartof(e, q):
            tau += q.get_flow()
    return tau

# print(edge_flow(G, (1, 2)))
# print(edge_flow(G, (2, 3)))
# print(edge_flow(G, (2, 6)))
# print(edge_flow(G, (3, 4)))
# print(edge_flow(G, (4, 5)))
# print(edge_flow(G, (4, 6)))
# print(edge_flow(G, (6, 7)))
# print_and_exit()


# \forall(v_i, v_j) \in {\bf E};
# o_{lij}=\tau_{ij}+\epsilon_{lij}

# a_{lij} = \begin{cases}
#   1 & (v_i, v_j) \in {\bf E} にセンサ s_l \in {\bf S} を設置 \\
#   0 & otherwise
# \end{cases}

# \forall s_l \in {\bf S} , \forall ( v_i , v_j ) \in {\bf E};
# a_{lij} = a_{lji}

# \bigcup_{ij} \phi_{ij} = f \left( \bigcup_{lij} a_{lij} , \bigcup_{lij} o_{lij} \right)

# \delta_{ij} = \phi_{ij} - \tau_{ij}

# \delta_{total} = \sum_{\{ i, j; ( v_i, v_j ) \in {\bf E} \}} | \delta_{ij} |

# \mathop{\rm arg~min}\limits_{\bigcup_{lij} a_{lij}} E [ \delta_{total} ]

# \frac{1}{2} \sum_{\{ l; s_l \in {\bf S} \}} \sum_{\{ l, j; ( v_i, v_j ) \in {\bf E} \}} a_{lij} c_l \leqq C_{max}
