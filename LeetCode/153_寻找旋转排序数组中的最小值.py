def findMin(nums: [int]) -> int:
    """
    把握局部有序性的特征：
    1. 当子列表整体有序时，left就是最小的值
    2. 当左边有序时，最小值一定在右边 如:[3,4,5,6,0,1]
    3. 当右边有序时，比较mid与mid-1：若mid-1小，最小值在左边；否则mid就是最小值

    pass
    """
    if not nums:
        return None
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # 当子列表整体有序时，left就是最小的值
        if nums[left] <= nums[mid] <= nums[right]:
            return nums[left]
        # 左边有序
        elif nums[left] <= nums[mid]:
            left = mid + 1
        # 右边有序
        elif nums[mid] > nums[mid - 1]:
            right = mid - 1
        else:
            return nums[mid]

    return nums[left]


# print(findMin([1]))
# print(findMin([1, 2]))
# print(findMin([2, 3, 1]))
# print(findMin([2, 1]))
# print(findMin([3, 4, 5, 1, 2]))
# print(findMin([4, 5, 6, 7, 0, 1, 2]))

print(findMin([3, 1, 2]))
