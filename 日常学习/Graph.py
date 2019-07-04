class GraphError(TypeError):
    pass


class Graph(object): # 基本图类，采用邻接矩阵表示
    def __init__(self, mat, unconn = 0): # unconn参数是为无关联的情况提供一个特殊值，无关联的取值视情况而定。
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum: # 检查是否为方阵
                raise ValueError("Argument for class 'Graph' is bad.")
        self._mat = [mat[i][:] for i in range(vnum)] # 做mat的拷贝
        self._unconn = unconn
        self._vnum = vnum


    def vertex_num(self):
        return self._vnum


    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise GraphError("Adj-Matrix does not support 'add_vertex'.")


    def add_edge(self, vi, vj, val = 1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + "is not a valid vertex.")
        self._mat[vi][vj] = val


    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj): # 检测要添加的边的信息是否符合目前的矩阵要求
            raise GraphError(str(vi) + 'or' + str(vj) + "is not a valid vertex.")
        return self._mat[vi][vj]


    def out_edges(self, vi): # 输出某一顶点的出边信息
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn): # 分析某一顶点的出边信息，得到出边所到的顶点以及边的权值
            edges = []                
            for i in range(len(row)):
                if row[i] != unconn:
                    edges.append((i, row[i]))
            return edges
    

    def __str__(self):
        # ,\n而不是\n的原因是，
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nUnconnected:" + str(self._unconn)
        # "\nUnconnected:"是无关联情况的表示方式

gmat = [[0, 0, 3, 4],
        [2, 0, 0, 0],
        [4, 1, 0, 0],
        [2, 0, 1, 0],]


if __name__ == '__main__':
    gl = Graph(gmat, 0)
    print(str(gl), '\n')
    print(gl.out_edges(0))
    
        