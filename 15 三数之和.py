def threeSum1(nums: [int]) -> [[int]]:
    """
    Solution 1:
    将其看成两数之和，target = 0 - nums[i]

    Timeout：311/313 个通过测试用例 —— 最后执行的输入超时
    """
    n = len(nums)
    # 排序
    nums = sorted(nums)
    result = []
    for i in range(n):
        target = 0 - nums[i]
        d = set()
        for j in range(i + 1, n):
            k = target - nums[j]
            if k in d:
                vs = [nums[i], k, nums[j]]
                # 排序
                if vs not in result:
                    result.append(vs)
            else:
                d.add(nums[j])

    return result


def threeSum2(nums: [int]) -> [[int]]:
    """
    Solution 2:
    两指针法

    pass
    """
    result, i = [], 0
    n = len(nums)
    if not nums or n < 3:
        return []
    nums.sort()
    for i in range(n):
        # 右边的值都比num[i]大，所以和不可能为0
        if nums[i] > 0:
            break
        # 不重复计算一种初始值
        if i > 0 and nums[i] == nums[i - 1]: continue
        left = i + 1
        right = n - 1
        while left < right:
            cmp = nums[i] + nums[left] + nums[right]
            if cmp == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: left = left + 1
                left = left + 1
                while left < right and nums[right] == nums[right - 1]: right = right - 1
                right = right - 1

            elif cmp < 0:
                while left < right and nums[left] == nums[left + 1]:
                    left = left + 1
                left = left + 1

            else:
                while left < right and nums[right] == nums[right - 1]:
                    right = right - 1
                right = right - 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum2(nums)
for x in result:
    print(x)
