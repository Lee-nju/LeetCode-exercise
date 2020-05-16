def checkSubarraySum(nums: [int], k: int) -> bool:
    """
    Solution:
    (x + y) % k = (x % k + y % k) % k
    1. 对nums做一个处理，其中每个元素对k取余，若取余为0，返回true，否则进入下一步
    2. 将0..i位置的和放入python dict(hash表)d中
    3. 如果sum_of_subArray % k 在d中，返回true；否则将sum_of_subArray % k放入字典中
    4. 返回False

    时间复杂度: O(N) 空间复杂度:O(N)

    pass
    :param nums:
    :param k:
    :return:
    """
    if len(nums) == 1:
        return False

    if k == 0:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] == 0:
                return True

        return False

    d = dict()
    continue_zero = 0
    sum_of_subArray = 0
    for x in nums:
        # k不为0的情况下，滤过不做贡献的0
        if x % k == 0:
            if continue_zero == 1:
                return True
            continue_zero = 1
            continue

        continue_zero = 0
        sum_of_subArray = sum_of_subArray + x % k
        if sum_of_subArray % k == 0:
            return True
        if (sum_of_subArray - k) % k in d:
            return True
        else:
            d[sum_of_subArray % k] = 1

    return False


# print(checkSubarraySum([23, 2, 4, 6, 7], 6))
# print(checkSubarraySum([23, 2, 6, 4, 7], 6))
# print(checkSubarraySum([1, 1, 1, 1, 1], 6))
# print(checkSubarraySum([1, 1, 1, 0, 1], 0))
# print(checkSubarraySum([0], 0))
# print(checkSubarraySum([1, 0], 2))
# print(checkSubarraySum([0, 0], -1))
print(checkSubarraySum([1, 2, 12], 6))
# print(checkSubarraySum([0], -1))
# print(checkSubarraySum([0, 1, 0, 0, 1], 0))
