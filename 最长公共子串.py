def LCString(str1: str, str2: str):
    if not str1 or not str2:
        return [0, '']

    # longest：最长公共子序列的长度，lastCommonIndex：长度更新时，最后一个字符的位置
    longest, lastCommonIndex, lcs = 0, 0, ''
    dp = [[0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > longest:
                    longest = dp[i + 1][j + 1]
                    lastCommonIndex = i + 1
            else:
                dp[i + 1][j + 1] = 0

    return [longest, str1[(lastCommonIndex - longest): lastCommonIndex]]


print(LCString('1AB2345Cd', '12345EF'))
