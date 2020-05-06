def maxSubArray(nums: [int]) -> int:
    if not nums:
        return
    n = len(nums)
    cur = max_sub_array = nums[0]
    i = 1
    while i < n:
        if cur <= 0:
            cur = nums[i]
        else:
            cur = cur + nums[i]
        max_sub_array = max(max_sub_array, cur)
        i = i + 1

    return max_sub_array


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([-2, -3, -1, -5]))
