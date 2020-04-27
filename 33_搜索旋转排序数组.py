def search(nums: [int], target: int) -> int:
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # 右边有序
        elif nums[mid] < nums[right]:
            # 右边有序的情况下，target如果在右边值之间，一定满足下面表达式
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        # 左边有序
        else:
            # 左边有序的情况下，target如果在左边值之间，一定满足下面表达式
            if nums[mid] > target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search([3, 4, 0, 1, 2], 2))
print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
