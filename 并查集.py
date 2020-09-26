class UnionSet:
    size = 0
    parent = []

    def __init__(self, size):
        self.size = size
        self.parent = list(range(size))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        else:
            # 增加v的父亲是u这条关系
            self.parent[v] = u
