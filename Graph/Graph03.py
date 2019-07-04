from Graph02 import *
from SStack import SStack


def DFS_seq(graph, v0):
    vnum = graph.vertex_num()
    visited = [0]*vnum # 生成访问记录，以供检测。
    visited[v0] = 1 # visited记录已访问顶点
    dfs_seq = [v0] # Dfs_seq记录遍历序列
    st = SStack()
    st.push((0, graph.out_edges(v0))) # 入栈(i, edges),说明下次应访问边edges[i]，即压入了某个顶点的所有出边信息
    while not st.is_empty(): # 循环一遍后再看：运用和“先进后出，后进先出”的特点，我们访问完v0后会先去访问v顶点，而不是i+1顶点
        i, edges = st.pop() # 将栈中的顶点的初始计算点和出边信息取出。
        if i < len(edges): # 查看是否有边，以及有几个边
            v, e = edges[i] # 获取出边点的信息以及边的权重
            st.push((i + 1, edges)) # 下次再访问这个点的时候将访问edges[i+1]，即访问下一个边
            if visited[v] == 0: # 检测出边点v是否被访问过，若未被访问，访问其记录可达顶点。
                dfs_seq.append(v) # 将被访问的v添加进序列。
                visited[v] = 1# 记录v已经被访问
                st.push((0, graph.out_edges(v))) # 压入v，访问v的出边点
        # 一直循环，直到所有点被访问。
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

v0 v1 v2 v4 v3 v7 v6 v8 v5 v9
v0 v2 v1 v4 v3 v7 v6 v8 v5 v9
v0 v2 v4 v1 v3 v7 v6 v8 v5 v9
v0 v1 v4 v2 v3 v7 v6 v8 v5 v9
