def permute(nums: [int]) -> [[int]]:
    if not nums:
        return []
    n = len(nums)
    if n == 1:
        return [nums]
    res = []
    backtrack([], nums, res)
    return res


def backtrack(prefix: [int], nums: [int], res):
    """
    Solution：
    前缀不断的在增加，直到后缀nums的长度为2时，res中加入两组排列：[prefix + nums] and [prefix + nums[::-1]]

    :param prefix: 前缀
    :param nums: 当前数组
    :param res: 结果数组
    :return:
    """
    n = len(nums)
    if n == 2:
        res.append(prefix + nums)
        res.append(prefix + nums[::-1])
    else:
        for i in range(n):
            tmp = [*prefix, nums[i]]
            backtrack(tmp, nums[0: i] + nums[(i + 1):], res)


res = permute([1, 2, 3, 4])
print(len(res))
print(res)
