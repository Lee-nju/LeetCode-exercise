def subarraySum(nums: [int], k: int) -> int:
    """
    设置一个键值表d: key='从0-i的位置的和'，value='和为key出现的次数'
    如:nums = [1,1,1,-1,1,1,-2], k = 2
    假设当前位置为i，结果res = 0, sum_of_subArray = sum(nums[0..i])
    1. 查看k-sum_of_subArray是否在d中，如果在：res = res + d[sum_of_subArray - k]；否则res不变
    2. 将x放入d中，如果x在d中: d[x] = d[x] + 1；否则: d[x] = 1
    3. 查看k是否在d中，如果在:res = res + d[k]；否则res不变
    4. 返回res

    时间复杂度: O(N) 空间复杂度:O(N)

    pass
    :param nums:
    :param k:
    :return:
    """
    d = dict()
    res = sum_of_subArray = 0
    for x in nums:
        sum_of_subArray = sum_of_subArray + x
        if (sum_of_subArray - k) in d:
            res = res + d[sum_of_subArray - k]
        if sum_of_subArray in d:
            d[sum_of_subArray] = d[sum_of_subArray] + 1
        else:
            d[sum_of_subArray] = 1

    if k in d:
        res = res + d[k]

    return res


print(subarraySum([1, 1, 1, -1, 1, 1, -2], 2))
