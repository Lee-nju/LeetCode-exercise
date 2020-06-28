def wordBreak(s: str, wordDict) -> bool:
    """
    典型的递归问题:
    当s前一部分能与字典中某个关键字匹配时，假设是i位置之前。
    转换成其子问题，这种匹配的结果就变成了: wordBreak(s[i+1:], wordDict)的结果
    可能有多种匹配方式，每种匹配方式都试一次，
        假如某种方式能匹配上，直接返回True
        否则，继续试其他的匹配方式，直到结束。

    :param s:
    :param wordDict:
    :return:
    """
    # 当字符为空，表示匹配完成
    if not s:
        return True
    else:
        i = 0
        # 从第一个位置往后，看有没有匹配上的可能；这里换种方式也可以，即从每个关键字出发，匹配上了进入子问题
        while i < len(s):
            # 转换成子问题
            if s[:(i + 1)] in wordDict:
                # 如果匹配上了，返回True
                if wordBreak(s[i + 1:], wordDict):
                    return True
            i = i + 1

        return False


def wordBreak2(s: str, wordDict) -> bool:
    """
    动态规划：
    s[i:] 能否匹配上的结果取决于，之前能否匹配到i位置，以及之后能否匹配到最后的位置
    初始化长度比s大1的一个数组res，都是False；res[0]=True
    1. 从0位置往后看，对于字典中每个关键字，0位置之后能匹配的对应位置赋值为 True
    2. 从下一个 True 的位置 i 往后看，对于字典中每个关键字，i位置之后能匹配的对应位置赋值再为 True
    3. 直到 res[-1] == True 时，返回 True 并结束
    4. 否则，res每个元素都更新过时，返回 False 并结束

    N:s的长度 M:字典的大小
    时间复杂度: O(M*N)  超过98.36%
    空间复杂度: O(N)

    :param s:
    :param wordDict:
    :return:
    """
    res = [False] * (len(s) + 1)
    res[0] = True
    idx = 0
    while idx < len(s) + 1:
        if res[idx]:
            for key in wordDict:
                idx2 = idx + len(key)
                if s[idx: idx2] == key:
                    res[idx2] = True

            if res[-1]:
                return True

        idx = idx + 1

    return False


# print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
# print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
# print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))

print(wordBreak2(s="leetcode", wordDict=["leet", "code"]))
print(wordBreak2(s="applepenapple", wordDict=["apple", "pen"]))
print(wordBreak2(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
