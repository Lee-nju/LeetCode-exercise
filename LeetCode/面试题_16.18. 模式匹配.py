import re


def patternMatching(pattern: str, value: str) -> bool:
    """
    解题思路：利用正则表达式直接求解，关键是正则表达式中的 \1 \2

    一、 字符的匹配：
    \1 表示正则表达式中第一个匹配到的字串
    \2 表示正则表达式中第二个匹配到的字串

    那么，给出几个表示的例子。
    1. 'aabb' 可以表示为 '(\w*)\1(\w*)\2'
    2. 'aaaaabb' 可以表示为 '(\w*)\1\1\1\1(\w*)\2'
    3. 'bbaa' 可以表示为 '(\w*)\1(\w*)\2'
    4. 'bababa' 可以表示为 '(\w*)(\w*)\1\2\1\2'

    二、 题目要求：a和b匹配的字符不能一样
    res = pa.fullmatch(value) 表能否匹配到
    1. 特殊情况
        如果：res.lastindex == 2，表明：pattern 里面有 'a' 也有 'b'
        判断 'a' 和 'b' 匹配的字串是否一致，即 res.group(1) == res.group(2)
        如果是 res.group(1) == res.group(2)，返回 False

    2. 其他情况
        如果 pattern 能匹配上，返回 True
        否则返回 False

    :param pattern:
    :param value:
    :return:
    """
    if not pattern:
        return not value

    reg = '(\\w*)'
    ch = pattern[0]
    i = 1
    while i < len(pattern) and pattern[i] == ch:
        reg = reg + '\\1'
        i = i + 1

    if i < len(pattern):
        reg = reg + '(\\w*)'
        for j in range(i + 1, len(pattern)):
            if pattern[j] == ch:
                reg = reg + '\\1'
            else:
                reg = reg + '\\2'

    print(reg)
    pa = re.compile(reg)
    res = pa.fullmatch(value)
    if res:
        if res.lastindex == 2 and res.group(1) == res.group(2):
            return False
        else:
            return True
    else:
        return False


print(patternMatching('abab', 'dogcatdogcatcat'))
print(patternMatching("abba", "dogcatcatdog"))
print(patternMatching("abba", "dogdogdogdog"))
print(patternMatching("aaaa", "dogcatcatdog"))
# a b 相等的例子
print(patternMatching("ab", ""))
print(patternMatching("abab", ""))
print(patternMatching("bbba", "xxxxxx"))
print(patternMatching("bbbaa", "xxxxxx"))
