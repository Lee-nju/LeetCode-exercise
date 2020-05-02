def subarraysWithKDistinct(A: [int], K: int) -> int:
    """
    Solution：
        判断由每个数开头的子数组最远能扩多远
        1. 假设当前位置为i，j是从i开始最初达到K个不同的整数位置，从j的位置往后扩，直到A[j]不在A[i:j]中（K+1个不同的整数）
        2. 不断扩的过程也是res累加的过程

    时间复杂度：O(N^2) 空间复杂度:O(1)

    TimeOut
    :param A:
    :param K:
    :return:
    """

    res, n = 0, len(A)
    for i in range(n):
        j = i + 1
        diff_num = 1
        # 找j的位置
        while j < n and diff_num < K:
            if A[j] not in A[i:j]:
                diff_num = diff_num + 1
            j = j + 1

        # 说明存在以当前位置为开头的子数组，其中有K个不同的整数
        if diff_num == K:
            res = res + 1
            while j < n and A[j] in A[i: j]:
                j = j + 1
                res = res + 1

    return res


def subarraysWithKDistinct2(A: [int], K: int) -> int:
    """
    Solution：
        判断由每个数开头的子数组最远能扩多远
        1. 假设当前位置为i，j是从i开始最初达到K个不同的整数位置，k是首次走到K+1个不同的整数位置
        2. 位置为i的好数组个数为：k-j+1
        3. 下一步令i=i+1:
            3.1 若A[i]在A[i+1:j]里面，A[i+1]=A[i];
            3.2 若不在, 判断A[i]是否在A[j:k]里面：
                若不在，令j=k+1,重新找k的位置
                若在，从j开始在A中找第一个等于A[i]的位置h，j=h+1
        4. 当k==n时，只移动i即可，当i在A[i+1:]时，A[i+1]=1，否则结束

    时间复杂度：O(N^2) 空间复杂度:O(1)

    TimeOut
    :param A:
    :param K:
    :return:
    """
    res, n = 0, len(A)
    i, j = 0, 1
    diff_num = 1
    # 找第一个j的位置
    while j < n and diff_num < K:
        if A[j] not in A[i:j]:
            diff_num = diff_num + 1
        j = j + 1

    # 上一个位置出发的好数组个数
    res_last = 0
    # 找第一次k的位置
    k = j
    if diff_num == K:
        res_last = res_last + 1
        while k < n and A[k] in A[i: j]:
            k = k + 1
            res_last = res_last + 1
    else:
        return 0

    # i=0 的好数组
    res = res_last
    # j < k 一定成立，只判断k即可
    while i < n and k < n:
        if A[i] in A[i + 1:j]:
            pass
        elif A[i] in A[j: k]:
            j = A.index(A[i], j, k) + 1
            res_last = k - j + 1
        else:
            k = j = k + 1
            res_last = 1
            while k < n and A[k] in A[i + 1: j]:
                k = k + 1
                res_last = res_last + 1

        res = res + res_last
        # 说明存在以当前位置为开头的子数组，其中有K个不同的整数
        i = i + 1

    while A[i] in A[i + 1:]:
        if A[i] in A[i + 1:j]:
            pass
        elif A[i] in A[j:]:
            j = A.index(A[i], j, k) + 1
            res_last = k - j + 1
        res = res + res_last
        i = i + 1

    return res


# print(subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
# print(subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
# print(subarraysWithKDistinct2([1, 2, 1, 2, 3], 2))
# print(subarraysWithKDistinct2([1, 2, 1, 3, 4], 3))
# print(subarraysWithKDistinct2([2, 1, 1, 1, 2], 1))
print(subarraysWithKDistinct2([2, 1, 2, 1, 2], 2))
