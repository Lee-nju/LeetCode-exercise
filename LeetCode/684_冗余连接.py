class Solution:
    def findRedundantConnection(self, edges: [[int]]) -> [int]:
        parent = list(range(len(edges) + 1))

        def findp(x):
            if x != parent[x]:
                parent[x] = findp(parent[x])
            return parent[x]

        for x, y in edges:
            xp, yp = findp(x), findp(y)
            if xp != yp:
                parent[yp] = xp
            else:
                return [x, y]


print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
