def threeSum(nums: list) -> list:
    """
    将其看成两数之和，target = 0 - nums[i]

    """
    n = len(nums)
    result = []
    for i in range(n):
        target = 0 - nums[i]
        d = set()
        for j in range(i + 1, n):
            k = target - nums[j]
            if k in d:
                vs = [nums[i], k, nums[j]]
                # 排序
                vs = sorted(vs)
                if vs not in result:
                    result.append(vs)
            else:
                d.add(nums[j])

    return result


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
for x in result:
    print(x)
