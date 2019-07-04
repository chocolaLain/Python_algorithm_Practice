from Graph import *
inf = float("inf") # 表示无穷大


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: # 检查是否方阵
                raise ValueError("Argument for 'GraphA' is bad.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn


    def add_vertex(self): # 增加新顶点时安排一个新编号
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1


    def add_edge(self, vi, vj, val = 1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge into empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                " is not a valid vertex.")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj: # 修改 mat[vi][vj] 的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj: # 原无到 vj 的边，退出循环在正确位置加入
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))


    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                " is not a valid vertex.")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn


    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._mat[vi]
gmat = [[0, 0, 3, 4],
        [2, 0, 0, 0],
        [4, 1, 0, 0],
        [2, 0, 1, 0]]


if __name__ == '__main__':
    g3 = GraphAL(gmat, 0)
    print(str(g3))
    g3.add_edge(0, 3, 5)
    g3.add_edge(1, 3, 6)
    g3.add_edge(3, 1, 9)
    x = g3.add_vertex()
    print(x)
    g3.add_edge(x, 1, 5)
    g3.add_edge(2, x, 6)
    print(str(g3))