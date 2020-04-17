def lengthOfLongestSubstring(s: str) -> [str, int]:
    """
    两指针法：
    1.记录当前的字串 2.记录最长的字串 3.不断更新左右指针，直到右指针到达n-1

    pass
    """
    # 防止s为空
    if not s:
        return 0
    longestStr = cStr = s[0]
    l, r = 0, 1
    n = len(s)
    while r < n:
        if s[r] not in cStr:
            cStr = cStr + s[r]
            if len(cStr) > len(longestStr):
                longestStr = cStr
        else:
            index = cStr.index(s[r]) + 1
            l = l + index
            cStr = s[l: (r + 1)]
        r = r + 1

    return longestStr, len(longestStr)


str = 'wpwkew'
s, sLen = lengthOfLongestSubstring(str)
print(s, sLen)
