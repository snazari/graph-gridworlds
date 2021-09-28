from graph_tool.all import *
from itertools import product

class graph_gridworld:
    """
    A graph-tool based gridworld. Current limitation is it only produces NxN gridworlds.
    """
    def __init__(self,name):
        """Constructor for graph_gridworld"""
        self.name = name

    def create_lattice(self,N):
        """
        Creates a lattice graph and puts state property map over it
        :param N: order of graph
        :return:
            g - the graph object
            map - the mapping of vertex indicies to states i.e., v --> (i,j)
            mapinv - the inverse of map, i.e., (i,j) --> v
        """
        g = lattice([N,N])
        n = list(g.get_vertices())
        m = list(product(set(range(N)), set(range(N))))
        map = dict(zip(m,n)) # map the state (i,j) to node index a \in [0, i \times j]
        mapinv = dict(zip(n,m))
        vmap = g.new_vertex_property("object")
        g.vp.state = vmap
        for v in g.iter_vertices():
            g.vp.state[v] = mapinv[v]
        return g, map, mapinv

    def get_neighbors(self, vertex,graph,imap):
        """
        input a vertex index, return neighboring states (i+i,j),(i-1,j),(i,j+1),(i,j-1)
        :param vertex:
        :param graph:
        :param imap:
        :return:
        """
        neighbors = list()
        for i in graph.get_all_neighbors(vertex):
            neighbors.append(imap[i])
        return neighbors

#TODO create functions get_neighbors_by_index(), get_neighbors_by_state()

if __name__ == '__main__':
    gg = graph_gridworld("First-GG")
    g, map, mapinv = gg.create_lattice(N=10)
    print(map)
    print(mapinv)
    print(g.vp.state[42])
    print(map[g.vp.state[42]])
    print(g.get_all_neighbors(map[g.vp.state[42]]))
    n = get_neighbors(22,g,mapinv)
    print(n)
