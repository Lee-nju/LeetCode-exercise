def maxProduct(nums: [int]) -> int:
    """
    Solutions:
    设当前位置为i，res储存整个的子数组最大乘积值，cur_positive储存当前子数组最大乘积正值，cur_negative存负值
    1. 当num[i]为正数时：
        cur_positive == 0 时: cur_positive=num[i]; 否则: cur_positive = nums[i] * cur_positive
        更新结果值: res = max(cur_positive, res)
        同理更新cur_negative，cur_negative不为0时: cur_negative = nums[i] * cur_negative
    2. 否则：
        用cur_positive来更新cur_negative和res
        用cur_negative更新cur_positive和res
    3. 更新cur_positive和cur_negative，当其绝对值小于1时，会被之后的乘积抛弃，即置为0
    4. 返回res

    时间复杂度:O(N) 空间复杂度:O(1)

    pass
    :param nums:
    :return:
    """
    res = -1000000000
    cur_positive = cur_negative = 0

    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            # 如果正最大乘积为0，正最大乘积置为nums[i]
            if cur_positive == 0:
                cur_positive = nums[i]
            else:
                cur_positive = nums[i] * cur_positive

            res = max(cur_positive, res)
            # 如果负最大乘积不为0，就乘上整数
            if cur_negative != 0:
                cur_negative = nums[i] * cur_negative

        else:
            tmp = cur_negative
            # 用cur_positive来更新cur_negative和res
            if cur_positive != 0:
                cur_negative = nums[i] * cur_positive
            else:
                cur_negative = nums[i]

            res = max(cur_negative, res)

            # 用cur_negative更新cur_positive和res
            if tmp != 0:
                cur_positive = nums[i] * tmp
                res = max(cur_positive, res)
            else:
                cur_positive = 0

        if -1 < cur_negative < 0:
            cur_negative = 0
        if 0 < cur_positive < 1:
            cur_positive = 0

        i = i + 1

    return res


# print(maxProduct([2, 3, -2, 4, -1]))
# print(maxProduct([2, 3, -2, 4]))
# print(maxProduct([-2, 0, -1]))
# print(maxProduct([-1, -1]))
# print(maxProduct([2, -5, -2, -4, 3]))
print(maxProduct([2, -5, -2, 2, -4, 3]))
print(maxProduct([-1, -2, -9, -6]))
