from Graph import *
inf = float("inf") # 表示无穷大


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: # 检查是否方阵
                raise ValueError("Argument for 'GraphA' is bad.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)] # 根据出边信息得出邻接表
        self._vnum = vnum
        self._unconn = unconn


    def add_vertex(self): # 增加新顶点时安排一个新编号
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1 # 返回新编号


    def add_edge(self, vi, vj, val = 1):
        if self._vnum == 0: # 考虑没有顶点时的空图情况
            raise GraphError("Cannot add edge into empty graph.")
        if self._invalid(vi) or self._invalid(vj): # 调用邻接矩阵的判断边是否符合要求的方法
            raise GraphError(str(vi) + ' or ' + str(vj) +
                " is not a valid vertex.")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj: # 修改 mat[vi][vj] 的值
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj: # 因为得到的出边顶底的下标是递增的，所以这意味着可能原本就没有 vj 的边，退出循环在正确位置加入
                break
            i += 1
        self._mat[vi].insert(i, (vj, val)) # 添加边


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

gmat = [[0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],]


if __name__ == '__main__':
    g3 = GraphAL(gmat, 0)
    print(str(g3))
 