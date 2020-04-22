def Manacher(s: str) -> int:
    """马拉车算法实现: 求最长回文字串的长度"""
    if not s:
        return 0
    # 处理数组
    s = '#' + "#".join(s) + '#'
    n = len(s)
    res = 0
    c = r = -1
    b_arr = [0] * n
    i = 0
    while i < n:
        if i < r:
            b_arr[i] = b_arr[2 * c - i] if b_arr[2 * c - i] < r - i else r - i

        while i + b_arr[i] + 1 < n and i - b_arr[i] - 1 >= 0:
            if s[b_arr[i] + i + 1] == s[i - b_arr[i] - 1]:
                b_arr[i] = b_arr[i] + 1
            else:
                break

        if b_arr[i] + i > r:
            r = b_arr[i] + i
            c = i

        res = max(b_arr[i], res)
        i = i + 1

    return res


print(Manacher('babad'))
print(Manacher('feabaaabacd'))
