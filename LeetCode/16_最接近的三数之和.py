import random


def threeSumClosest(nums: [int], target: int) -> int:
    """
    暴力解法： 找到所有的三个数的和，求距离 target 最小的值

    时间复杂度: O(N ^ 2)

    :param nums:
    :param target:
    :return:
    """

    res = 10000000
    # arr = [0] * 3
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                s = nums[i] + nums[j] + nums[k]
                if abs(res - target) > abs(s - target):
                    res = s
                    # arr[0], arr[1], arr[2] = nums[i], nums[j], nums[k]

    # print(arr)
    return res


def threeSumClosest2(nums: [int], target: int) -> int:
    """
    解题思路： 排序 + 双指针
    1. 对原数组排序，从小到大
    2. 固定一个位置i，看i位置被选中的情况下，再选哪两个最优
        2.1 j指向i的下一个位置，k指向最后一个位置，s = nums[i] + nums[j] + nums[k]
        2.2 如果s小于target，j往后移动j++；否则，k往前移动，k--
        2.3 在这过程中，记录所有 abs(s - target) 最小的一个
        2.4 当 s == target 时，可跳出外层循环，因为这就是最优解

    时间复杂度: O(N ^ 2)
    空间复杂度为： O(log N) —— 快速排序的划分位置所需的额外空间

    :param nums:
    :param target:
    :return:
    """
    nums.sort()
    res = 100000000
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if abs(res - target) > abs(s - target):
                res = s
            if s < target:
                j = j + 1
            elif s > target:
                k = k - 1
            else:
                break

        if res == target:
            break

    return res


# print(threeSumClosest([-1, 2, 1, -4, -2], -8))
# print(threeSumClosest2([-1, 2, 1, -4, -2], -8))

print(threeSumClosest([0, 5, -1, -2, 4, -1, 0, -3, 4, -5], 1))
print(threeSumClosest2([0, 5, -1, -2, 4, -1, 0, -3, 4, -5], 1))

# 对数器
# for i in range(100):
#     length = random.randint(3, 100)
#     nums = [0] * length
#     for j in range(length):
#         nums[j] = random.randint(-1000, 1000)
#
#     target = random.randint(-10000, 10000)
#     case1 = threeSumClosest(nums, target)
#     case2 = threeSumClosest2(nums, target)
#
#     if case1 != case2:
#         print('--------------------------------')
#         print("数组为： ", nums, 'target 为：', target)
#         print("case1: ", case1)
#         print('case2: ', case2)
#         print()
