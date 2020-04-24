def ZeroOnePack():
    """0 1 背包问题"""
    m, n = 10, 4
    c = [0, 2, 3, 4, 7]
    w = [0, 1, 3, 5, 9]
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):  # 枚举前 i 个物品
        for v in range(1, m + 1):  # 枚举体积
            dp[i][v] = dp[i - 1][v]  # 不选第 i 个物品
            if v >= c[i]:  # 第 i 个物品的体积必须小于 v 才能选
                dp[i][v] = max(dp[i][v], dp[i - 1][v - c[i]] + w[i])

    return dp  # 返回前 n 个物品的最大值


def ZeroOnePack2():
    """
    原dp空间复杂度为O(MN)，因为当前位置的值只与上一行的前面位置有关
    所以从后往前遍历，将空间复杂度优化成 O(M)

    """
    m, n = 10, 4
    # 重量
    w = [2, 3, 4, 7]
    # 价值
    c = [1, 3, 5, 9]
    dp = [0 for i in range(m + 1)]
    for i in range(n):
        for j in range(m, 0, -1):
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j - w[i]] + c[i])

    return dp


def CompletePack():
    """完全背包问题：每个物品可以取多次的最大价值"""
    m, n = 12, 4
    # 重量
    w = [2, 3, 4, 7]
    # 价值
    c = [1, 3, 5, 9]
    dp = [0 for i in range(m + 1)]
    for i in range(n):
        for j in range(m, 0, -1):
            if j >= w[i]:
                # 第i个物品最多取 j // w[i] 件
                for k in range(1, j // w[i] + 1):
                    dp[j] = max(dp[j], dp[j - k * w[i]] + k * c[i])

    return dp


def CompletePack2():
    """完全背包问题的优化 O(MN)"""
    m, n = 12, 4
    # 重量
    w = [2, 3, 4, 7]
    # 价值
    c = [1, 3, 5, 9]
    dp = [0 for i in range(m + 1)]
    for i in range(n):
        for j in range(m + 1):
            if j >= w[i]:
                # 从前往后遍历，相当于可以取多件
                dp[j] = max(dp[j], dp[j - w[i]] + c[i])

    return dp


# 0 1背包问题
print(ZeroOnePack2())
# 优化空间后的0 1背包问题
print(ZeroOnePack()[-1])
# 完全背包问题
print(CompletePack())
# 完全背包问题的优化
print(CompletePack2())
