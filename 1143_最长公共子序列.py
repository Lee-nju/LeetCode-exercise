def longestCommonSubsequence(text1: str, text2: str) -> int:
    if text1 and text2:
        n1, n2 = len(text1), len(text2)
        res = [0 for i in range(n1 + 1)]
        for i in range(n2):
            # last更新为0，即：text1 = '' 时，res的取值
            last = 0
            for j in range(n1):
                # 在res[i][j]更新之前，将其存到last，为后面做准备
                tmp = res[j + 1]
                if text1[j] == text2[i]:
                    res[j + 1] = last + 1
                else:
                    res[j + 1] = max(res[j], res[j + 1])
                last = tmp

        return res[-1]
    else:
        return 0


print(longestCommonSubsequence("abcde", 'ace'))
print(longestCommonSubsequence("abc", 'abc'))
print(longestCommonSubsequence("abc", 'def'))
print(longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
