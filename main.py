from graph_tool.all import *
from itertools import product

class graph_gridworld:
    """
    A graph-tool based gridworld. Current limitation is it only produces NxN gridworlds.
    """
    def __init__(self, name):
        """Constructor for graph_gridworld"""
        self.name = name

    def create_lattice(self, N):
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

    def get_action_set(self, vertex, graph, imap):
        """
        input a vertex index, return neighboring states (i+i,j),(i-1,j),(i,j+1),(i,j-1)
        :param vertex: single graph vertex index, e.g., vertex = 3
        :param graph:  the graph object
        :param imap:   the inverse mapping (mapinv) (i,j)-->v
        :return:       returns the neighboring _states_, e.g., [(i+i,j),(i-1,j),(i,j+1),(i,j-1)]
        """
        neighbors = list()
        for i in graph.get_all_neighbors(vertex):
            neighbors.append(imap[i])
        return neighbors

    def plan_route(self,g,u_s,v_s,map):
        """
        Given a graph, g, and a starting state, u_s, plan the shortest distance to target state v_s.
        :param g:
        :param u:
        :param v:
        :param map:
        :return: a shortest list of states from u_s to v_s
        """
        u = map[u_s]
        v = map[v_s]
        vertex_list, edge_list = shortest_path(g,u,v)
        return [g.vp.state[i] for i in vertex_list]


#TODO create functions get_neighbors_by_index(), get_neighbors_by_state()

if __name__ == '__main__':
    gg = graph_gridworld("First-GG")
    g, map, mapinv = gg.create_lattice(N=5)
    print(map)
    print(mapinv)
    print(g.vp.state[12])
    print(map[g.vp.state[12]])
    print(g.get_all_neighbors(map[g.vp.state[12]]))
    n = gg.get_action_set(12,g,mapinv)
    print(n)
    u_s = (0,0)
    v_s = (3,3)
    l = gg.plan_route(g,u_s,v_s,map)
    print(l)
    print(l)