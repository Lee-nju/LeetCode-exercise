import random


def heap_sort(nums: [int]):
    """
    堆排序
    1. 调整为大根堆
        1.1 调整过程看作递增的heapInsert过程，假设当前插入元素为i，从i=1开始。
        1.2 i-1之前的数组已调整为大根堆，与父节点值比较，如果大于父节点值上调，直到不能上调为止(下标为0，或比父节点值小)

    2. 堆顶元素与数组第i大的位置交换，无序数组的长度减1 （相当于堆顶元素出堆）
        2.1 i 初始化为len(nums) - 1，即最大值的下标，nums[0] 与 nums[i]交换
        2.2 交换过后，堆顶元素下调heapify，直到再次调整为堆结构
        2.3 i = i - 1，重复2过程，直到 i>0 为止

    工程上使用较少，因为常数项大且不稳定
    :param nums:
    :return:
    """
    if not nums or len(nums) < 2:
        return

    # 堆调整
    for i in range(1, len(nums)):
        heap_insert(nums, i)

    # 最大值元素的下标
    i = len(nums) - 1
    # 最大值元素下标为0时结束
    while i > 0:
        # 堆顶元素与第i大下标元素交换
        nums[0], nums[i] = nums[i], nums[0]
        # 向下调整
        heapify(nums, i)
        i = i - 1


def heapify(nums: [int], end: int):
    """
    向下调整函数。
    从第一个位置往下调整，每次调整需比较两次
    1. 父节点相互比较，大者胜出
    2. 子节点与父节点值较大者比较：
        子节点值大，结束向下的过程
        父节点较大者仍大，当前节点与较大者交换，回到1

    :param nums:
    :param end:
    :return:
    """
    index = 0
    left = 2 * index + 1
    while left < end:
        # larger 取父节点值较大的下标
        larger = left if left + 1 >= end or nums[left] >= nums[left + 1] else left + 1
        # 如果父节点最大值大于当前节点，当前节点往下交换，否则结束循环
        if nums[index] < nums[larger]:
            nums[index], nums[larger] = nums[larger], nums[index]
        else:
            break

        # 下标迭代
        index = larger
        left = 2 * index + 1


def heap_insert(nums: [int], index: int):
    # 父节点下标通过这种运算是可以为负值的
    f_index = (index - 1) // 2
    # 限制节点会循环，将f_index限制在非负数
    while f_index >= 0 and nums[index] > nums[f_index]:
        nums[index], nums[f_index] = nums[f_index], nums[index]
        index = f_index
        f_index = (index - 1) // 2


# 随机生成5组随机数组
for i in range(5):
    length = random.randint(5, 20)
    nums = [0] * length
    for j in range(length):
        nums[j] = random.randint(0, 60)

    # 生成的随机数组用于排序
    print('------------排序前------------')
    print(nums)
    heap_sort(nums)
    print('------------排序后------------')
    print(nums)
    print()

# debug
nums = [26, 58, 25, 59, 17, 35, 49, 45, 53, 12, 12]
print('------------排序前------------')
print(nums)
heap_sort(nums)
print('------------排序后------------')
print(nums)
print()
