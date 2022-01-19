#! python3
# graph.py

import random
class Graph(dict):
    def __init__(self, vs = list(), es = list()):
        '''Create a new graph. vs is a list of vertices; es is a list of edges'''
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        '''Add v to the graph.'''
        self[v] = dict()

    def add_edge(self, e):
        '''Add e to the graph by adding entry in both directions.
         If there is already an edge connecting the vertices the new edge replaces it.'''
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        try:
            return self[v1][v2]
        except KeyError:
            return None

    def remove_edge(self, e):
        try:
            v, w = e
            del self[v][w]
            del self[w][v]
        except KeyError:
            print('No such edge found')

    def vertices(self):
        vertices = list()
        for v in self.keys():
            vertices.append(v)
        return vertices

    def edges(self):
        edges = set()
        for v in self.keys():
            for edge in self[v].values():
                edges.add(edge)
        return list(edges)

    def out_vertices(self, v):
        out_v = list()
        for w in self[v]:
            out_v.append(w)
        return out_v

    def out_edges(self, v):
        out_e = list()
        for e in self[v].values():
            out_e.append(e)
        return out_e

    def add_all_edges(self):
        for v in self.keys():
            for w in self.keys():
                if v != w:
                    e = Edge(v, w)
                    self.add_edge(e)

    def add_regular_edges(self, n):
        for v in self:
            while len(self[v].keys()) < n:
                for w in self:
                    if v != w:
                        if len(self[w]) < n:
                            e = Edge(v, w)
                            self.add_edge(e)

    def is_connected(self):
        v_found = set()
        vertices = set(self.vertices())
        v = random.choice(list(self.keys()))
        marked_vertices = self.mark(v, v_found)
        if marked_vertices == vertices:
            return True
        else:
            return False

        
    def mark(self, v, v_found):
        for w in self[v]:
            if w not in v_found:
                v_found.add(w)
                self.mark(w, v_found)
        return v_found

    def is_connected_2(self):
        queue = list()
        marked = list()
        v = random.choice(list(self.keys()))
        marked.append(v)
        for w in self[v]:
            queue.append(w)
        for w in queue:
            if not w in marked:
                for k in self[w]:
                    queue.append(k)
                marked.append(w)

        vertices = self.vertices()
        if vertices == marked:
            return True
        else:
            return False

    def add_random_edges(self, p):
        for v in self:
            for w in self:
                if v != w:
                    rand = random.random()
                    if p > rand:
                        e = Edge(v, w)
                        self.add_edge(e)
            
            

    
class Vertex(object):
    def __init__(self, label = ''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)'%repr(self.label)

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, *vs):
        return tuple.__new__(cls, vs)

    def __repr__(self):
        return 'Edge (%s, %s)'%(repr(self[0]),repr(self[1]))

    __str__ = __repr__


def random_graphs(g):
    data = dict()
    for i in range(100):
        connected_graphs = 0
        for t in range(10):
            k = g
            k.add_random_edges(i / 100)
            if k.is_connected():
                connected_graphs += 1
        data[i] = connected_graphs
    return data
        
if __name__ == '__main__':
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    g = Graph([v, w], [e])
    a = Vertex('a')
    c = Edge(a, v)
    k = Graph([v, w, a])
