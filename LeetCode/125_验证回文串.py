import re


def is_valid(ch):
    """
    判断给定的单个字符是否为数字或字母

    :param ch:
    :return:
    """
    pattern = re.compile(r'^[0-9]|[a-zA-Z]$')
    result = pattern.match(ch)
    if result:
        return True
    else:
        return False


def isPalindrome(s: str) -> bool:
    """
    双指针法：当左右指针都指向合法字符（数字或字母）时：
    回文串一定会相等，非回文穿不一定相等

    :param s:
    :return:
    """
    if not s:
        return True

    i, j = 0, len(s) - 1
    while i < j:
        # 如果i位置的字符不是数字或字母，i往后移动
        while i < len(s) - 1 and not is_valid(s[i]):
            i = i + 1

        # 如果j位置的字符不是数字或字母，j往前移动
        while j > 0 and not is_valid(s[j]):
            j = j - 1

        if i >= j:
            break

        if s[i].lower() != s[j].lower():
            return False
        else:
            i = i + 1
            j = j - 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
