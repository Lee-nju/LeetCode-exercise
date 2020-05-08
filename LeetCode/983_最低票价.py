import math


def mincostTickets(days: [int], costs: [int]) -> int:
    """
    Solutions:
    从后往前遍历，res=[0..n+1]*0,下标表示当前位置,存储当前位置怎么买票最划算。
    1. 如果当前买一天的票才划算，就买1天的票
    2. 如果当前买7天的票和买30天的票都划算，和买1天的票比较取最小
    3. 如果当前买7天的票划算，和买1天的比较取最小
    4. 如果当前买30天的票的划算，和买1天的比较取最小
    5. 返回res[0]

    pass
    :param days:
    :param costs:
    :return:
    """
    m1, m2 = math.ceil(costs[1] / costs[0]), math.ceil(costs[2] / costs[0])
    n = len(days)
    res = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if (i + m1 - 1 < n and days[i + m1 - 1] - days[i] < 7) and (i + m2 - 1 < n and days[i + m2 - 1] - days[i] < 30):
            j = i + m1
            while j < n and days[j] - days[i] < 7:
                j = j + 1

            k = i + m2
            while k < n and days[k] - days[i] < 30:
                k = k + 1
            res[i] = min(res[j] + costs[1], res[k] + costs[2], res[i + 1] + costs[0])
        elif i + m1 - 1 < n and days[i + m1 - 1] - days[i] < 7:
            j = i + m1
            while j < n and days[j] - days[i] < 7:
                j = j + 1

            res[i] = min(res[j] + costs[1], res[i + 1] + costs[0])
        elif i + m2 - 1 < n and days[i + m2 - 1] - days[i] < 30:
            k = i + m2
            while k < n and days[k] - days[i] < 30:
                k = k + 1

            res[i] = min(res[k] + costs[2], res[i + 1] + costs[0])
        else:
            res[i] = costs[0] + res[i + 1]

    return res[0]


# days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
# costs = [2, 7, 15]
# print(mincostTickets(days, costs))
print(mincostTickets([1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45]))
