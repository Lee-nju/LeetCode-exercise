def maxSlidingWindow(nums: [int], k: int) -> [int]:
    """
    滑动窗口最大值：
    设置3个指针: 分别是左右指针i,j和max_index指针，左右指针同时往前移动
    1. 当最右指针指向的值小于max_index的值，max_index更新为j
    2. 否则，当左指针大于max_index时，max_index失效，在[i, j]中重新找最大值的下标
    3. 将max_index对应的值加入res

    时间复杂度：O(N * k)

    pass
    :param nums:
    :param k:
    :return:
    """
    res = []
    max_index = 0
    i, j = 0, 1
    while j < k and j < len(nums):
        if nums[max_index] <= nums[j]:
            max_index = j
        j = j + 1

    res.append(nums[max_index])
    if k >= len(nums):
        return res

    while j < len(nums):
        i = i + 1
        if nums[max_index] <= nums[j]:
            max_index = j
        elif i > max_index:
            max_index = i
            for m in range(i, j + 1):
                if nums[max_index] <= nums[m]:
                    max_index = m

        j = j + 1
        res.append(nums[max_index])

    return res


# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 1))
# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 8))
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
