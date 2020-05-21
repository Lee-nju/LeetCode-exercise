def max_pre_subArray(strs: [str]) -> str:
    i, res = 0, ''
    while True:
        ch = strs[0][i]
        for str in strs[1:]:
            if i > len(str) - 1 or ch != str[i]:
                return res

        i = i + 1
        res = res + ch


print(max_pre_subArray(['abcd', 'abd', 'abg']))
print(max_pre_subArray(['abcdefbef', 'abcd', 'abcg']))
print(max_pre_subArray(['ef', 'abcd', 'abcg']))
