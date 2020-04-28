def countSubstrings(s: str) -> int:
    """
    以当前位置向左右扩，如果是回文串，res加1，直到当前位置扩到边界或不等时

    pass
    """
    # 数组处理
    ms = '#' + '#'.join(s) + '#'
    res, n = 0, len(ms)
    for i in range(n):
        j = 1 if ms[i] == '#' else 0
        while i + j < n and i - j >= 0:
            if ms[i + j] == ms[i - j]:
                res = res + 1
                # 跳过虚轴
                j = j + 2
            else:
                break

    return res


print(countSubstrings('abc'))
