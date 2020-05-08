def maximalSquare(matrix: [[str]]) -> int:
    """
    Solutions:
    从小到大的单调栈stack,存储左边比其小的下标和自身下标。
    每次以当前行做底，square表示出以当前行做底的形状
    如：matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    square[i=0..3]
    i=0: [1, 0, 1, 0, 0]
    i=1: [2, 0, 2, 1, 1]
    i=2: [3, 1, 3, 2, 2]
    i=3: [4, 0, 0, 3, 0]

    遍历square中的每个元素，设当前位置为j，如果square[j]小于等于栈顶元素，将[j-1, j]压栈。
    否则，栈顶元素出栈赋值给lk，计算当前的正方形面积值：
    横坐标长为j-lk[0]-1,纵坐标长为square[k]，最大面积的边长为: square_len = min(j-lk[0]-1, square[k])
    最大面积为：square_len^2 与 max_square 的较大者
    直到栈顶为空，或栈顶元素代表的square[lk[1]]不大于square[j]

    对于栈中剩下的元素k，横坐标长为n-lk[0]-1,纵坐标长为square[k]:
    square_len = min(n-lk[0]-1, square[lk[1]])
    max_square = max(max_square, square_len * square_len)


    时间复杂度O(M*N) 空间复杂度O(N)

    pass
    :param matrix:
    :return:
    """
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    square = [0] * n
    max_square = 0
    for i in range(m):
        stack = []
        for j in range(n):
            if matrix[i][j] == '1':
                square[j] = square[j] + 1
            else:
                square[j] = 0

            if not stack or square[stack[-1][1]] <= square[j]:
                stack.append([j - 1, j])
            else:
                lk = []
                while stack and square[stack[-1][1]] > square[j]:
                    lk = stack.pop(-1)
                    square_len = min(j - lk[0] - 1, square[lk[1]])
                    max_square = max(max_square, square_len * square_len)

                stack.append([lk[0], j])

        while stack:
            lk = stack.pop(-1)
            square_len = min(n - lk[0] - 1, square[lk[1]])
            max_square = max(max_square, square_len * square_len)

    return max_square


# matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
# print(maximalSquare(matrix))
# print(maximalSquare([["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]]))
# print(maximalSquare([["0", "1"], ["0", "1"]]))
print(maximalSquare(
    [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]))
