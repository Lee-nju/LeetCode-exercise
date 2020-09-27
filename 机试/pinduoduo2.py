from collections import deque
import functools


def compare(x, y):
    if x[0] > y[0] or (x[0] == y[0] and x[1] > y[1]):
        return 1
    elif x[0] == y[0] and x[1] == y[1]:
        return 0
    return -1


def shortest_distance(matrix, si, sj):
    queue = deque()
    queue.append([si, sj])
    shortest_distance = 0
    n, m = len(matrix), len(matrix[0])
    while queue:
        shortest_distance += 1
        k = len(queue)
        while k > 0:
            i, j = queue.popleft()
            if i > 0:
                if matrix[i - 1][j] == 'T':
                    return shortest_distance
                elif matrix[i - 1][j] == '0':
                    queue.append([i - 1, j])
            if i < n - 1:
                if matrix[i + 1][j] == 'T':
                    return shortest_distance
                elif matrix[i - 1][j] == '0':
                    queue.append([i + 1, j])
            if j > 0:
                if matrix[i][j - 1] == 'T':
                    return shortest_distance
                elif matrix[i][j - 1] == '0':
                    queue.append([i, j - 1])
            if j < m - 1:
                if matrix[i][j + 1] == 'T':
                    return shortest_distance
                elif matrix[i][j + 1] == '0':
                    queue.append([i, j + 1])

            k -= 1


def pinduoduo():
    try:
        N, M = map(int, input().split())
        matrix = []
        for i in range(N):
            s = input().strip()
            matrix.append(s)

        shortest_dis = 1e8
        index = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 'X':
                    tmp_dis = shortest_distance(matrix, i, j)
                    if tmp_dis < shortest_dis:
                        shortest_dis = tmp_dis
                        index = [str(i) + str(j)]
                    elif tmp_dis == shortest_dis:
                        index.append(str(i) + str(j))

        print(shortest_dis)
        index.sort()
        res = ''
        for x in index:
            res += x

        for i in range(len(res)):
            if i != len(res) - 1:
                print(res[i], end=' ')
            else:
                print(res[i], end='\n')
    except:
        print('出错！！！')


a = [[1, 2], [1, 1], [1, 0], [0, 1]]
a.sort(key=functools.cmp_to_key(compare))
print(a)
