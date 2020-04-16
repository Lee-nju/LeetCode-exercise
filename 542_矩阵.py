def updateMatrix(matrix):
    """
    思路：
    对于每个不为0的数，根据邻近的最小值更新，值更新为邻近的最小值+1， 直到数组不再变化为止

    :param matrix: 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
    :return: 返回距离矩阵
    """
    if isinstance(matrix[0], int):
        ma = [matrix[i] for i in range(len(matrix))]
        while True:
            for i in range(len(matrix)):
                if matrix[i] > 0:
                    ma[i] = matrix[i - 1] + 1 if matrix[i - 1] < matrix[i + 1] else matrix[i + 1] + 1
                if ma == matrix:
                    return ma
                else:
                    # 深拷贝
                    for i in range(len(matrix)):
                        for j in range(len(matrix[0])):
                            matrix[i][j] = ma[i][j]

    # 深拷贝
    ma = [[] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ma[i].append(matrix[i][j])

    while True:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                value = []
                if matrix[i][j] > 0:
                    if i > 0:
                        value.append(matrix[i - 1][j])
                    if i < len(matrix) - 1:
                        value.append(matrix[i + 1][j])
                    if j > 0:
                        value.append(matrix[i][j - 1])
                    if j < len(matrix[0]) - 1:
                        value.append(matrix[i][j + 1])

                    ma[i][j] = leastNum(value)

        if ma == matrix:
            return ma
        else:
            # 深拷贝
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][j] = ma[i][j]


def leastNum(value: list) -> int:
    """
    :param list
    :return list中最小的int再加1
    """
    if len(value) == 1:
        return value[0] + 1

    k = value[0]
    for i in range(1, len(value)):
        if k > value[i]:
            k = value[i]

    return k + 1


# 案例
case = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
# 打印案例
for x in case:
    print(x)
print('--------------------------------')

# 执行并打印
m = updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                  [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]])
for x in m:
    print(x)
