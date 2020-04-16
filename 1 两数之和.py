def twoSum1(nums: list, target: int) -> list:
    """
    Solution 1:
    利用哈希下标的原理，但内存消耗太大，需要一个和target一样的内存

    超出时间限制: [50000000,3,2,4,50000000] 100000000
    """
    length = len(nums)
    k = nums[0]
    for x in nums[1:]:
        if k > x:
            k = x
    if k < 0:
        k = -k
        target = target + 2 * k
    else:
        k = 0

    value = [-1 for i in range(target + 1)]
    for i in range(length):
        mx = nums[i] + k
        if mx > target:
            continue
        else:
            x = target - mx
            if value[x] != -1:
                return [value[x], i]
            else:
                value[mx] = i


def twoSum2(nums: list, target: int) -> list:
    """
    Solution 2:
    暴力求解 O(n2)

    能过，但很慢
    """
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum3(nums: list, target: int) -> list:
    """
    Solution 3:
    利用字典: 时间快了很多

    """
    d = {}
    n = len(nums)
    for x in range(n):
        if target - nums[x] in d:
            return [d[target - nums[x]], x]
        else:
            d[nums[x]] = x


nums = [-3, 4, 3, 90]
target = 0

value = twoSum2(nums, target)
print(value)
