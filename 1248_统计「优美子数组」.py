def numberOfSubarrays(nums: [int], k: int) -> int:
    """
    假设i为当前位置，以i结尾的[优美子数组]的个数是确定的：
    1. num[i] = 0 <= i及之前位置的奇数小于k
    2. num[i] = l + 1 <= i为第一次正好有k个奇数的子数组，l为其第一个奇数在nums中的下标
    3. nums[i]为偶数 => res[i] = res[i - 1]
    4. num[i]为奇数 => res[i] = single[l] - single[l - 1]

    pass
    """
    n = len(nums)
    # 存数组中奇数的下标
    single = []
    # 初始的结果
    res = []
    i = 0
    while i < n:
        if nums[i] % 2 == 1:
            if len(single) == k - 1:
                single.append(i)
                i = i + 1
                break
            else:
                single.append(i)

        res.append(0)
        i = i + 1

    if len(single) != k:
        return 0

    res.append(single[0] + 1)
    # l指向连续数组的最左奇数位置
    l = 0
    while i < n:
        if nums[i] % 2 == 0:
            res.append(res[-1])
        else:
            single.append(i)
            v = single[l + 1] - single[l]
            res.append(v)
            l = l + 1
        i = i + 1

    return sum(res)


nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
print(numberOfSubarrays(nums, k))
