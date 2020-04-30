import sys


def test1(s: str) -> int:
    """
    解法1：递归的方式
    :param s: 字符串
    :return: 返回总的排列数
    """
    n = len(s)
    if len(set(s)) == n:
        return factor(n)
    res = set()
    for i in range(n):
        recursive(s[0:i] + s[i + 1: n], s[i], res)

    return len(res)


def factor(n):
    k = 1
    for i in range(2, n + 1):
        k = k * i
    return k


def recursive(s, tmp, res):
    if len(s) == 2:
        res.add(tmp + s)
        res.add(tmp + s[::-1])
    else:
        for i in range(len(s)):
            recursive(s[0:i] + s[i + 1: len(s)], tmp + s[i], res)


def CalcAllPermutation(s: str):
    """
    解法2：字典序算法
    1. 如果当前排列是124653,找它的下一个排列的方法是，从这个序列中从右至左找第一个左邻小于右邻的数，
    2. 如果找不到，则所有排列求解完成，如果找得到则说明排列未完成。
       本例中将找到46,计4所在的位置为i,找到后不能直接将46位置互换，而又要从右到左到第一个比4大的数，
    3. 本例找到的数是5，其位置计为j，将i与j所在元素交换125643
    4. 然后将i+1至最后一个元素从小到大排序得到125346，这就是124653的下一个排列。

    """
    n = len(s)
    case = [i for i in range(n)]
    res = set()
    while True:
        tmp = ''
        for i in case:
            tmp = tmp + s[i]
        res.add(tmp)
        k1 = n - 2
        # 找第一个左邻小于右邻的下标
        while k1 >= 0:
            if case[k1] < case[k1 + 1]:
                break
            k1 = k1 - 1
        # 如果没有左邻小于右邻的数 跳出
        if k1 == -1:
            break
        # 从右往左找第一个k1大的数的下标k2, k2在k1的右边
        k2 = n - 1
        while k2 > k1:
            if case[k1] < case[k2]:
                break
            k2 = k2 - 1
        # 交换下标
        case[k1], case[k2] = case[k2], case[k1]
        case[k1 + 1:] = sorted(case[k1 + 1:])

    print(list(res))
    return len(res)


if __name__ == "__main__":
    """实现有重复字符的字符串排列"""
    line = sys.stdin.readline().strip()
    print(CalcAllPermutation(line))
