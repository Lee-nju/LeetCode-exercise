def spiralOrder(matrix: [[int]]) -> [int]:
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    index, layer = 0, 1
    res = [0] * m * n
    while index < m * n:
        i = j = layer - 1
        res[index] = matrix[i][j]
        index = index + 1
        while j < n - layer:
            j = j + 1
            res[index] = matrix[i][j]
            index = index + 1

        while i < m - layer:
            i = i + 1
            res[index] = matrix[i][j]
            index = index + 1

        if index == m * n:
            break

        while j > layer - 1:
            j = j - 1
            res[index] = matrix[i][j]
            index = index + 1

        while i > layer:
            i = i - 1
            res[index] = matrix[i][j]
            index = index + 1

        layer = layer + 1

    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(spiralOrder([[1]]))
print(spiralOrder([[1], [2], [3], [4]]))
