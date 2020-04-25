def reversePairs(nums: [int]) -> int:
    """
    插入排序：O(N^2)

    TimeOut
    """
    res = 0
    for i in range(1, len(nums)):
        j = i
        while j - 1 >= 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            res = res + 1
            j = j - 1

    # print(nums)
    return res


def reversePairs2(nums: [int]) -> int:
    """
    归并排序：分治思想 O(N logN)

    """
    if not nums or len(nums) == 1:
        return 0
    else:
        # 全局的临时数组，减少创建和销毁数组的开销
        tmp = [0 for x in nums]
        # 保留原数组
        # copy = [x for x in nums]
        res = divide(nums, 0, len(tmp) - 1, tmp)
        print(nums)
        return res


def divide(nums, left, right, tmp):
    if left == right:
        return 0
    else:
        mid = left + (right - left) // 2
        left_pairs = divide(nums, left, mid, tmp)
        right_pairs = divide(nums, mid + 1, right, tmp)

        # 优化：如果左右数组已经是有序的了，就不需要在输出了
        if nums[mid] <= nums[mid + 1]:
            return left_pairs + right_pairs

        cross_pairs = conquer(nums, left, mid, right, tmp)
        return left_pairs + right_pairs + cross_pairs


def conquer(nums, left, mid, right, tmp) -> int:
    # 拷贝数组进临时数组，
    for i in range(left, right + 1):
        tmp[i] = nums[i]

    i, j = left, mid + 1
    res = 0
    k = left
    while i <= mid or j <= right:
        if i == mid + 1:
            nums[k] = tmp[j]
            j = j + 1
            k = k + 1
        elif j == right + 1:
            nums[k] = tmp[i]
            i = i + 1
            k = k + 1
        elif tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i = i + 1
            k = k + 1
        else:
            nums[k] = tmp[j]
            j = j + 1
            k = k + 1
            res = res + mid - i + 1

    return res


print(reversePairs2([3, 5, 7, 9, 2, 4, 6, 8]))
