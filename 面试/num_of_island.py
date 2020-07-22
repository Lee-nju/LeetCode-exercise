from collections import deque


def num_of_island(num: [[int]]):
    """
    问题：给定一个0 1矩阵，1表示陆地，0表示水，求此矩阵有多少块陆地

    Solution：
        设定一个是否被判断过的矩阵，假设遍历到[i,j]的位置，如果其不属于之前的任何一个岛屿（没被review过）
        且其值为1（表示是陆地），那么就说明我们发现了一块新岛屿，res += 1；同时，将属于此岛屿的所有陆地标
        记上reviewed，标记的方法可以用深度优先，也可以用广度优先，这里选择广度。

    :param num:
    :return:
    """
    if not num or not num[0]:
        return
    m = len(num)
    n = len(num[0])
    res = 0
    is_reviewed = [[False for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if is_reviewed[i][j] or num[i][j] == 0:
                continue

            traverse(num, is_reviewed, start_point=[i, j])
            res = res + 1

    return res


def traverse(num, is_reviewed, start_point: [int, int]):
    # is_reviewed[start_point[0]][start_point[1]] = True
    queue = deque()
    queue.append(start_point)
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        is_reviewed[x][y] = True
        if x + 1 < len(num) and y < len(num[0]) and not is_reviewed[x + 1][y] and num[x + 1][y] == 1:
            is_reviewed[x][y] = True
            queue.append([x + 1, y])
        if x < len(num) and y + 1 < len(num[0]) and not is_reviewed[x][y + 1] and num[x][y + 1] == 1:
            is_reviewed[x][y + 1] = True
            queue.append([x, y + 1])
        if x - 1 >= 0 and y < len(num[0]) and not is_reviewed[x - 1][y] and num[x - 1][y] == 1:
            is_reviewed[x - 1][y] = True
            queue.append([x - 1, y])
        if x < len(num) and y - 1 >= 0 and not is_reviewed[x][y - 1] and num[x][y - 1] == 1:
            is_reviewed[x][y - 1] = True
            queue.append([x + 1, x])


num = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
print(num_of_island(num))
