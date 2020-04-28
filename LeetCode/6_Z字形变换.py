def convert(s: str, numRows: int) -> str:
    """pass"""
    if numRows == 1:
        return s
    st = ['' for i in range(numRows)]
    i, k = 0, 1
    for ch in s:
        st[i] = st[i] + ch
        if i + k == numRows:
            k = -k
            i = i - 1
        elif i + k == -1:
            k = -k
            i = i + 1
        else:
            i = i + k

    result = ''.join(st)
    return result


print(convert('LEETCODEISHIRING', 3))
