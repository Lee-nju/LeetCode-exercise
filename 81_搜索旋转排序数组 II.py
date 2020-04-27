def search(nums: [int], target: int) -> bool:
    """
    相较第33题，多了一步处理；
    即：如果中间值和左值或右值相等，让其往左移动，移动到第一个左值不等于中间值的位置

    时间复杂度为O(N) 如[1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    """
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target or nums[left] == target or nums[right] == target:
            return True

        # 左边有序
        if nums[left] <= nums[mid]:
            try:
                # 如果中间值和左值相等，让mid其往左移动，移动到第一个左值不等于中间值的位置
                # 同时让left往右移动，移动到移动到最后一个左值不等于left的位置
                while mid > left and nums[mid] == nums[mid - 1]:
                    mid = mid - 1
                if mid > left:
                    mid = mid - 1
                while left < mid and nums[left] == nums[left + 1]:
                    left = left + 1
            except:
                return False
            if nums[left] < target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        # 右边有序
        else:
            try:
                # 如果中间值和左值或右值相等，让其往左移动，移动到第一个左值不等于中间值的位置
                while mid < right and nums[mid] == nums[mid + 1]:
                    mid = mid + 1
                if mid < right:
                    mid = mid + 1
                while mid < right and nums[right] == nums[right - 1]:
                    right = right - 1
            except:
                return False
            if nums[mid] <= target < nums[right]:
                left = mid
            else:
                right = mid - 1

    return False


def search2(nums: [int], target: int) -> bool:
    """
    不用分那么多情况，简单的去掉重复的值，进入下一次循环即可

    时间复杂度：O(N)
    """
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target or nums[left] == target or nums[right] == target:
            return True

        # 左边有序
        if nums[left] <= nums[mid]:
            # 让left往右移动一个单位
            if left < mid and nums[left] == nums[mid]:
                left = left + 1
                continue
            if nums[left] < target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        # 右边有序
        else:
            if mid < right and nums[mid] == nums[right]:
                right = right - 1
                continue
            if nums[mid] <= target < nums[right]:
                left = mid
            else:
                right = mid - 1

    return False


# print(search([1, 1, 3, 1], 3))
# print(search([1, 3, 1, 1], 3))
# print(search([1], 0))
# print(search([1, 1], 0))
# print(search([3, 1], 0))
# print(search([1, 3, 1, 1, 1], 3))

print(search2([1, 1, 3, 1], 3))
print(search2([1, 3, 1, 1], 3))
print(search2([1], 0))
print(search2([1, 1], 0))
print(search2([3, 1], 0))
print(search2([1, 3, 1, 1, 1], 3))
