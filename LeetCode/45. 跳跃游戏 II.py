def jump(nums: [int]) -> int:
    """
    Solution:
    数组res=[-1]*(n-1)表到当前位置最小的跳步数,从前往后遍历,设当前位置为i,当前res[i]步最远的位置为 farthest_reach
    1. 如果i+nums[i] >= n-1, return res[i] + 1
    2. 否则:
        若i+nums[i] > farthest_reach, res[farthest_reach, i+nums[i]]中替换为res[i]+1
        否则res无变化
    3. 当step增加时，farthest_reach 小于当前下标时，说明不能到达当前下标，结束；

    时间复杂度: O(N) 空间复杂度:O(N)
    pass

    :param nums:
    :return:
    """
    # 空数组
    if not nums:
        return
    n = len(nums)

    # 单元素数组
    if n == 1:
        return 0

    # 从第一个位置跳不到后面
    if nums[0] == 0:
        return

    # 从第一个位置可以直接到最后
    if nums[0] >= n - 1:
        return 1

    # [4,1,3,2,0,0,1] 初始化 res=[1,1,1,1,1,-1]
    steps = [1] * (nums[0] + 1) + [-1] * (n - 2 - nums[0])
    farthest_reach = nums[0]
    for i in range(1, n):
        if farthest_reach < i:
            return
        cur_max_reach = i + nums[i]
        if cur_max_reach >= n - 1:
            return steps[i] + 1
        elif cur_max_reach > farthest_reach:
            steps[farthest_reach + 1: cur_max_reach + 1] = [steps[i] + 1] * (cur_max_reach - farthest_reach)
            farthest_reach = cur_max_reach


def jump2(nums: [int]) -> int:
    """
    Solution:
    从后往前, 当前位置为i, step[i]表示从位置i到位置n-1的最小步数
    1. 如果: step[i] + i >= n - 1: step[i] = 1
    2. 否则, step[i]等于[i+1, step[i] + i]中的最小不为-1的值再加1
    3. step[0] == -1, 返回None; 否则返回step[0]

    时间复杂度: O(N^2) 空间复杂度:O(N)
    passed: 90/92

    :param nums:
    :return:
    """
    if not nums:
        return
    n = len(nums)
    # 单数组
    if n == 1:
        return 0
    # 从第一个位置调不到后面
    if nums[0] == 0:
        return
    steps = [-1] * (n - 1)
    i = n - 2
    while i >= 0:
        if nums[i] == 0:
            steps[i] = -1
        elif nums[i] + i >= n - 1:
            steps[i] = 1
        else:
            k = search_least(steps[i + 1: i + nums[i] + 1])
            if k != -1:
                steps[i] = k + 1
            else:
                steps[i] = -1
        i = i - 1

    if steps[0] != -1:
        return steps[0]


def search_least(res):
    v = -1
    for x in res:
        # 如果 x!=-1，且v==-1，说明是v第一次需要更新的时候
        if x != -1 and (v == -1 or x < v):
            v = x
    return v


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 2, 1, 1, 4]))
print(jump([2, 2, 1, 0, 4]))
