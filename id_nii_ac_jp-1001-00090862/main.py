#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    pass


if __name__ == '__main__':
    main()

# {\bf G} ( {\bf V}, {\bf E} )

# {\bf V} = \{ v_1, v_2, ..., v_i \}

# {\bf E} = \{ (v_1, v_2), (v_2, v_3), (v_2, v_6), ..., (v_i, v_j) \}

# b(i,j,k)= \begin{cases}
#   1 & ( v_i , v_j ) \in p_k \\
#   0 & otherwise
# \end{cases}

# \forall(v_i, v_j) \in {\bf E};
# \tau_{ij}=\sum_{k=1}^{|P|}b(i,j,k)\theta_k

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
