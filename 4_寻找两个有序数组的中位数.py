def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    """
    1.将两个数组合并成一个数组，对合并后的数组做一次快速排序，时间复杂度正好为O(log(m + n))
    2.寻找有序数组的中位数很简答，就是中间下标的平均数

    pass
    """
    if not nums1:
        nums1 = nums2
    elif not nums2:
        pass
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    m1 = n // 2
    m2 = (n - 1) // 2
    return (nums1[m1] + nums1[m2]) / 2


print(findMedianSortedArrays([1, 3], [2]))
