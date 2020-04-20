from collections import deque


def numIslands(grid: [[str]]) -> int:
    """
    广度优先遍历

    pass
    """
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])
    visited = [[False for j in range(col)] for i in range(row)]
    priorityQueue = deque()
    res = 0
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and grid[i][j] != '0':
                res = res + 1
                visited[i][j] = True
                priorityQueue.append([i, j])
                while priorityQueue:
                    index = priorityQueue.popleft()
                    if index[0] > 0 and not visited[index[0] - 1][index[1]] and grid[index[0] - 1][index[1]] != '0':
                        priorityQueue.append([index[0] - 1, index[1]])
                        visited[index[0] - 1][index[1]] = True
                    if index[1] > 0 and not visited[index[0]][index[1] - 1] and grid[index[0]][index[1] - 1] != '0':
                        priorityQueue.append([index[0], index[1] - 1])
                        visited[index[0]][index[1] - 1] = True
                    if index[0] < row - 1 and not visited[index[0] + 1][index[1]] and grid[index[0] + 1][index[1]] != '0':
                        priorityQueue.append([index[0] + 1, index[1]])
                        visited[index[0] + 1][index[1]] = True
                    if index[1] < col - 1 and not visited[index[0]][index[1] + 1] and grid[index[0]][index[1] + 1] != '0':
                        priorityQueue.append([index[0], index[1] + 1])
                        visited[index[0]][index[1] + 1] = True

    return res


test1 = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
test2 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
test2 = [[str(test2[i][j]) for j in range(5)] for i in range(4)]
print(numIslands(test2))
