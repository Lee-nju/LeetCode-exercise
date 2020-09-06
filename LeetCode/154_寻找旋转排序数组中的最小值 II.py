def findMin(nums: [int]) -> int:
    if not nums:
        return None

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # 右边单调有序时，最小值在左边
        if nums[mid] < nums[right]:
            right = mid
        # 当 mid == right 时，去掉最后一个 right，重新计算
        elif nums[mid] == nums[right]:
            right = right - 1
        # 否则，mid > right，最小值肯定在右边
        else:
            left = mid + 1

    return nums[left]


print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([2, 2, 2, 0, 1]))
print(findMin([3, 1, 1]))
print(findMin([3, 3, 1, 3]))
print(findMin([3, 3, 3, 1]))
print(findMin([3, 3, 3, 3, 3, 3, 3, 3, 1, 3]))
