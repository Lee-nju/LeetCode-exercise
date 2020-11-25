#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param grid char字符型二维数组
# @return int整型
#
from _collections import deque


class Solution:
    def numIslands(self, grid):
        # write code here
        m, n = len(grid), len(grid[0])
        res = 0

        visited = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        ix, iy = queue.popleft()
                        if ix + 1 < m and grid[ix + 1][iy] == '1' and not visited[ix + 1][iy]:
                            queue.append((ix + 1, iy))
                            visited[ix + 1][iy] = True
                        if ix - 1 >= 0 and grid[ix - 1][iy] == '1' and not visited[ix - 1][iy]:
                            queue.append((ix - 1, iy))
                            visited[ix - 1][iy] = True
                        if iy + 1 < n and grid[ix][iy + 1] == '1' and not visited[ix][iy + 1]:
                            queue.append((ix, iy + 1))
                            visited[ix][iy + 1] = True
                        if iy - 1 >= 0 and grid[ix][iy - 1] == '1' and not visited[ix][iy - 1]:
                            queue.append((ix, iy - 1))
                            visited[ix][iy - 1] = True

                    res += 1

        return res


print(Solution().numIslands(
    [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '1']]))
