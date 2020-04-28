def isMatch(s: str, p: str) -> bool:
    i = j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j] or p[j] == '.':
            i = i + 1
            j = j + 1
        elif p[j] == '*':
            if s[i] == p[j - 1]:
                i = i + 1
            else:
                j = j + 1
        elif j + 1 < len(p) and p[j + 1] == '*':
            i = i + 1
            j = j + 2

    return i == len(s) and j == len(p)


# print(isMatch('aa', 'a'))
# print(isMatch('aa', 'a*'))
# print(isMatch('aa', 'a.'))
print(isMatch('aab', 'c*a*b*'))
print(isMatch("mississippi", "mis*is*p*."))
print(isMatch("mississippi", "mis*is*ip*."))
print(isMatch('ab', '.*c'))
