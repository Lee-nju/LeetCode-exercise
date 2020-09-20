while 1:
    s = input()
    if s != '':
        str1 = input()
        str2 = input()
        n1, n2 = len(str1), len(str2)
        res = []
        for i in range(n1 + 1):
            res.append([0] * (n2 + 1))

        for i in range(n1):
            for j in range(n2):
                if str1[i] == str2[j]:
                    res[i + 1][j + 1] = res[i][j] + 1
                else:
                    res[i + 1][j + 1] = max(res[i + 1][j], res[i][j + 1])

        if res[-1][-1] != n2:
            print('No')
        else:
            score = 0
            i, j = n1, n2
            while i > 0 and j > 0:
                if str1[i - 1] == str2[j - 1]:
                    tmp = i
                    i -= 1
                    while i > 0 and str1[i] == str1[i - 1]:
                        tmp = i
                        i -= 1
                    score = score + tmp
                    j -= 1
                elif res[i - 1][j] == res[i][j - 1]:
                    i -= 1
                elif res[i - 1][j] < res[i][j - 1]:
                    j -= 1
                else:
                    i -= 1
            print('Yes')
            print(score)
    else:
        break

# test 1
# 6 3
# aabddc
# abc

# test 2
# 18 4
# aaaaabbbbbddddcccc
# abdc
