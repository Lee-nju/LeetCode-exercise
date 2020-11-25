def lengthOfLIS(nums):
    # write code here
    if not nums:
        return 0
    longest_len = 1
    for i in range(len(nums)):
        tmp_len, tmp_value = 1, nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] > tmp_value:
                tmp_value = nums[j]
                tmp_len += 1

        longest_len = max(longest_len, tmp_len)

    return longest_len


print(lengthOfLIS([10, 9, 2, 5, 3, 6, 101, 18]))
