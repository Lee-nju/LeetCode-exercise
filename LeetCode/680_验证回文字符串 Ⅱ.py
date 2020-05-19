def validPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i = i + 1
            j = j - 1
        else:
            s1, s2 = s[i + 1: j + 1], s[i: j]
            return s1 == s1[::-1] or s2 == s2[::-1]

    return True


# print(validPalindrome('aba'))
# print(validPalindrome('abca'))
a = 'abca'
b = a[1:3]
print(validPalindrome('abca'))
print(b[::-1])
