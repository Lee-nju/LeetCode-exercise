import sys


def test3(lines, K, N, R):
    """

    :param lines: 道路具体信息
    :param K: 费用
    :param N: 城市总数
    :param R: 道路总数
    :return:
    """
    # 标记城市是否走过了
    marked = [False] * (N + 1)
    cost_path = []
    deep_reverse(lines, K, N, 1, marked, 0, 0, cost_path)
    if not cost_path:
        return -1
    res = cost_path[0]
    for x in cost_path[1:]:
        if x[1] < res[1]:
            res = x

    return res[1]


def deep_reverse(lines, K, N, node, marked, cost, path, cost_path):
    """
    :param path:
    :param lines:
    :param K:
    :param N:
    :param node: 当前节点
    :param marked:
    :param res:
    :return:
    """
    marked[node] = True
    # 到达目的地
    if node == N:
        cost_path.append([cost, path])
    for line in lines:
        node_info = line.split()
        node_info = [int(x) for x in node_info]
        # 如果源点是node，且终点未走过
        if node_info[0] == node and not marked[node_info[1]]:
            # 如果总费用小于K，说明可以走
            if cost + node_info[-1] <= K:
                marked[node_info[1]] = True
                cost = cost + node_info[-1]
                path = path + node_info[-2]
                marked[node_info[1]] = True
                deep_reverse(lines, K, N, node_info[1], marked, cost, path, cost_path)
                marked[node_info[1]] = False
                cost = cost - node_info[-1]
                path = path - node_info[-2]
                marked[node_info[1]] = False


if __name__ == "__main__":
    K = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    R = int(sys.stdin.readline().strip())
    lines = []
    for i in range(R):
        lines.append(sys.stdin.readline().strip())

    print(test3(lines, K, N, R))
