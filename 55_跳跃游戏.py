from collections import deque


def canJump(nums: [int]) -> bool:
    """
    将当前能到达的点全部加入队列，格式为：[index, value]
    index为下标，value为nums中的值

    超时
    """
    if not nums:
        return False

    n = len(nums)
    if n == 1:
        return True
    res = deque()
    res.append([0, nums[0]])
    nums[0] = 0
    while res:
        cur = res.popleft()
        for i in range(1, cur[1] + 1):
            index = cur[0] + i
            if index >= n - 1 or nums[index] + index >= n - 1:
                return True
            if nums[index] != 0:
                res.append([index, nums[index]])
                nums[index] = 0

    return False


def canJump2(nums: [int]) -> bool:
    """
    不断更新能到达的最大值，如果最大值能大于等于n-1，返回True
    如果当前下标等于当前能到达的最大值，返回False

    时间复杂度o(N) 空间复杂度o(1)

    pass
    """
    if not nums:
        return False

    n = len(nums)
    if n == 1:
        return True
    max_reachable, i = nums[0], 1
    while i <= max_reachable:
        max_reachable = max(nums[i] + i, max_reachable)
        if max_reachable >= n - 1:
            return True
        i = i + 1

    return False


# print(canJump([2, 3, 1, 1, 4]))
print(canJump2([3, 2, 1, 0, 4]))
# print(canJump([0]))
# print(canJump([2, 0]))
