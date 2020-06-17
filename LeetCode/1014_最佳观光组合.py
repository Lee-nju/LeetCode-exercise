def maxScoreSightseeingPair(A: [int]) -> int:
    """
    解题思路：
    从前往后遍历，假设当前位置为i，维护一个最大价值：max_value
    1. max_value 初始化为 A[0]，每次前进一步，max_value = max_value - 1
    2. 考虑风景i被选，那么包含i的最佳观光组合大小就为：max_value + A[i]
    3. 那么结果更新为：res = max(res, max_value + A[i])
    4. max_value 更新： max_value = max(A[i], max_value)

    :param A:
    :return:
    """
    i, max_value = 1, A[0]
    res = 0
    while i < len(A):
        max_value = max_value - 1
        res = max(res, max_value + A[i])
        max_value = max(A[i], max_value)
        i = i + 1

    return res


print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
