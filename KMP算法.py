def KMP(str1: str, str2: str) -> int:
    """
    如果str1能包含str2，返回str1中完整匹配str2的初始位置，否则返回-1

    """
    next_arr = gen_next_arr(str2)
    i1 = i2 = 0
    n1, n2 = len(str1), len(str2)
    while i1 < n1 and i2 < n2:
        if str1[i1] == str2[i2]:
            i1 = i1 + 1
            i2 = i2 + 1
        elif i2 != -1:
            i2 = next_arr[i2]
        else:
            i1 = i1 + 1

    return i1 - n2 if i2 == n2 else -1


def gen_next_arr(str2: str) -> [int]:
    # 返回的结果数组
    next_arr = [-1, 0]
    # i表str2的下标；j表比较的位置，j位置不断移动，j位置的值与位置i-1的值比较，相等表示找到了，直到j==-1
    i, j, n = 2, 0, len(str2)
    while i < n:
        if str2[i - 1] == str2[j]:
            j = j + 1
            next_arr.append(j)
            i = i + 1
        elif j != -1:
            j = next_arr[j]
        else:
            j = 0
            next_arr.append(0)
            i = i + 1

    return next_arr


str1 = "abcabcabcabcabcdefg"
str2 = "abcabcde"
print(KMP(str1, str2))
