def productExceptSelf(nums: [int]) -> [int]:
    """
    两轮循环，分别求：前缀之积 和 后缀之积
    前缀之积：从前往后遍历，第一个变量的前缀之积为1
    后缀之积：从后往前遍历，最后一个变量的后缀之积为1
    
    :param nums: 
    :return: 
    """
    res = [0] * len(nums)
    i = res[0] = 1
    while i < len(nums):
        res[i] = nums[i - 1] * res[i - 1]
        i = i + 1

    # 存后缀之积
    tmp = 1
    j = len(nums) - 1
    while j >= 0:
        res[j] = res[j] * tmp
        tmp = tmp * nums[j]
        j = j - 1

    return res


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([0, 2, 3, 4]))
print(productExceptSelf([5, 7, 2, 3, 4]))
