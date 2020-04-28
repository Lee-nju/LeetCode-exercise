def longestPalindrome(s: str) -> str:
    """
    马拉车算法实现: 求最长回文字串

    pass
    """
    if not s:
        return ''
    # 处理数组
    ms = '#' + "#".join(s) + '#'
    n = len(ms)
    index1 = index2 = 0
    max_radius = 0
    c = r = -1
    b_arr = [0] * n
    i = 0
    while i < n:
        if i < r:
            b_arr[i] = b_arr[2 * c - i] if b_arr[2 * c - i] < r - i else r - i

        while i + b_arr[i] + 1 < n and i - b_arr[i] - 1 >= 0:
            if ms[b_arr[i] + i + 1] == ms[i - b_arr[i] - 1]:
                b_arr[i] = b_arr[i] + 1
            else:
                break

        if b_arr[i] + i > r:
            r = b_arr[i] + i
            c = i

        if b_arr[i] > max_radius:
            max_radius = b_arr[i]
            index1 = i - b_arr[i]
            index2 = i + b_arr[i]
        i = i + 1

    return s[index1 // 2: index2 // 2]


def longestPalindrome2(s: str) -> str:
    """
    暴力方法求解试试

    pass
    """
    if not s:
        return ''
    # 处理数组
    ms = '#' + "#".join(s) + '#'
    n = len(ms)
    index1 = index2 = 0
    res = 1
    i = 0
    while i < n:
        j = 1
        cur_res = 1
        while i - j >= 0 and i + j < n:
            if ms[i - j] == ms[i + j]:
                cur_res = cur_res + 2
                j = j + 1
            else:
                break
        if cur_res > res:
            index1 = i - j + 1
            index2 = i + j - 1
            res = cur_res

        i = i + 1

    return s[index1 // 2: index2 // 2]


# print(longestPalindrome('feabaaabacd'))
# print(longestPalindrome('babad'))
# print(longestPalindrome('babab'))
print(longestPalindrome2('babad'))
print(longestPalindrome2('feabaaabacd'))
