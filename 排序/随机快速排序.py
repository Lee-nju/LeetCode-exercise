import random


def random_quick_sort(nums: [int]):
    """
    充当一个盒子，作为程序的入口。
    工程上常用随机快速排序，快速排序分最好最差情况，而随机快速排序抹去了情况的讨论
    时间复杂度为: O(N * logN) 且 常数项低

    :param nums:
    :return:
    """
    if not nums or len(nums) < 2:
        return

    left, right = 0, len(nums) - 1
    quick_sort(nums, left, right)


def quick_sort(nums: [int], L: int, R: int):
    if L < R:
        # 随机产生一个数，并与最后一个数交换，随机快速排序的关键
        index = random.randint(L, R)
        # partition_val = nums[index]
        # 随机产生的下标与最后一个下标互换
        nums[index], nums[R] = nums[R], nums[index]
        # 分区，并返回less区右边界和more区左边界
        p1, p2 = partition(nums, L, R)
        quick_sort(nums, L, p1)
        quick_sort(nums, p2, R)


def partition(nums: [int], L: int, R: int) -> (int, int):
    if L < R:
        # 小于区初始化为L之前一个元素，大于区初始化为R
        less, more = L - 1, R
        i = L
        # 当下标与more区左边界碰上时结束
        while i < more:
            # nums[i] > nums[R]，仅交换，i不动
            if nums[i] > nums[R]:
                nums[i], nums[more - 1] = nums[more - 1], nums[i]
                more = more - 1
            else:
                if nums[i] < nums[R]:
                    nums[i], nums[less + 1] = nums[less + 1], nums[i]
                    less = less + 1
                # nums[i] <= nums[R]， i都需要往后走
                i = i + 1

        # 将作为划分的元素换到合适的位置
        nums[more], nums[R] = nums[R], nums[more]
        # 返回less区右边界和more区左边界
        return less, more + 1


# 随机生成5组随机数组
for i in range(5):
    length = random.randint(5, 20)
    nums = [0] * length
    for j in range(length):
        nums[j] = random.randint(0, 60)

    # 生成的随机数组用于排序
    print('------------排序前------------')
    print(nums)
    random_quick_sort(nums)
    print('------------排序后------------')
    print(nums)
    print()

# debug
nums = [47, 12, 57, 3, 43, 37, 6, 8, 7, 49, 35, 50, 51, 23, 1, 36, 43, 60, 30, 56]
print('------------排序前------------')
print(nums)
random_quick_sort(nums)
print('------------排序后------------')
print(nums)
print()
# print(partition(nums, 0, len(nums) - 1))
