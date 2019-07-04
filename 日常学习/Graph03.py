from Graph02 import *
from SStack import SStack


def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum
    visited[v0] = 1
    dfs_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i + 1, edges))
            if visited[v] == 0: # unvisited node
                dfs_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return dfs_seq

gmat1=[[1,1,0,0],
       [1,1,0,1],
       [1,0,1,0],
       [0,0,0,1]]

gmat2 = [[0, 0, 3, 4],
        [2, 0, 0, 0],
        [4, 1, 0, 0],
        [2, 0, 1, 0],]


if __name__ == '__main__':
    g1 = GraphAL(gmat1, 0)
    dfs1 = DFS_seq(g1, 0)
    print(dfs1)

    g2 = GraphAL(gmat2, 0)
    dfs2 = DFS_seq(g2, 0)
    print(dfs2, "\n")
