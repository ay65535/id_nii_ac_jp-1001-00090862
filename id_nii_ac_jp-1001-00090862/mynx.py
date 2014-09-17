#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx


class Graph(nx.Graph):
    def __init__(self, data=None, **attr):
        nx.Graph.__init__(self, data=data, **attr)
        self.paths = list()

    class Path:
        def __init__(self, data: list, flow: int=10):
            self.data = data
            self.flow = flow

        def get_path(self):
            return self.data

        def get_flow(self):
            return self.flow

    def add_path(self, nodes, **attr):
        nx.Graph.add_path(self, nodes, **attr)
        self.paths.append(self.Path(nodes))
