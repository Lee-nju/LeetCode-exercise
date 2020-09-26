class Solution:
    # 用边的数目来初始化并查集
    parent = []
    n = 0

    def findRedundantDirectedConnection(self, edges: [[int]]) -> [int]:
        self.n = len(edges)
        degrees = [0] * (self.n + 1)
        for edge in edges:
            degrees[edge[1]] += 1

        if 2 in degrees:
            removeEdges = []
            for i, edge in enumerate(edges[::-1]):
                if degrees[edge[1]] == 2:
                    # 将edges中可删除的边的下标放入e中
                    removeEdges.append(self.n - 1 - i)

            for removeEdge in removeEdges:
                if self.isTreeAfterRemoveEdge(edges, removeEdge):
                    return edges[removeEdge]

        # 如果没有入度为2的边
        else:
            return self.getRemoveEdge(edges)

    def isTreeAfterRemoveEdge(self, edges, removeEdge):
        self.initP()
        # 移除删掉的边
        remainEdge = edges[:removeEdge] + edges[removeEdge + 1:]
        for edge in remainEdge:
            px, py = self.findP(edge[0]), self.findP(edge[1])
            if px != py:
                self.parent[edge[1]] = px
            else:
                return False
        return True

    def getRemoveEdge(self, edges):
        self.initP()
        for edge in edges:
            px, py = self.findP(edge[0]), self.findP(edge[1])
            if px != py:
                self.parent[edge[1]] = px
            else:
                return edge

    def findP(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findP(self.parent[x])

        return self.parent[x]

    def initP(self):
        self.parent = list(range(self.n + 1))


print(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [5, 1]]))
print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
