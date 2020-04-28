def maxArea(height: [int]) -> int:
    """
    两指针法：
    i指向首，j指向尾；较小的数一定能找到以此为杆的最大的容器，然后i j不断靠近，直到相等

    """
    i, j = 0, len(height) - 1
    max_area = 0
    while i < j:
        if height[i] <= height[j]:
            cmp = (j - i) * height[i]
            max_area = cmp if cmp > max_area else max_area
            i = i + 1
        else:
            cmp = (j - i) * height[j]
            max_area = cmp if cmp > max_area else max_area
            j = j - 1

    return max_area


value = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(value))
