def isMatch(s: str, p: str) -> bool:
    """
    递归实现
    进行的步骤主要是对'*'的处理，
    1. 如果p为空，s是否为空就是结果
    2. 如果p不为空：
        2.1 p长度大于1且第二个字符为'*'，'*'有两种用法，一种是重复前面0次，一种是重复前面多次(可以分解为重复多个1次)
        2.2 否则，不用理会'*'的用法，直接判断 's为是否为空' 和 'p和s的第一个字符不匹配' ：
            如果满足其一，返回False；
            否则，去掉s和p匹配到的第一个字符，继续递归

    :param s:
    :param p:
    :return:
    """
    # 如果字符规律串为空，字符匹配串为空返回True，否则返回False
    if not p:
        return not s

    # 当p的长度大于1，并且p的第二个字符为'*'
    if len(p) > 1 and p[1] == '*':
        # 如果p和s的第一个字符能匹配，'*'可以有两种用法，一种是取0次，一种是取多次
        if s and (p[0] == s[0] or p[0] == '.'):
            # isMatch(s, p[2:])为'*'取0次，isMatch(s[1:], p)为'*'取多次的递归
            return isMatch(s, p[2:]) or isMatch(s[1:], p)
        else:
            # 当p和s的第一个字符不相等时，'*'只能取0次
            return isMatch(s, p[2:])

    # 如果p长度不大于1，或者p的第二个字符不为'*'
    else:
        # s为空 或 p和s的第一个字符不匹配，返回False即可
        if not s or (p[0] != s[0] and p[0] != '.'):
            return False
        else:
            # 否则去掉s和p匹配到的第一个字符，继续递归
            return isMatch(s[1:], p[1:])


def isMatch1(s: str, p: str) -> bool:
    """
    动态规划
    dp：动态矩阵 dp[i][j]：s的前i个元素能否被p的前j个元素所匹配
    1. 初始化dp：
        · dp的第一列除了dp[0][0]，其他为False；
        · dp的第一行有：dp[0][0] = True, dp[0][1] = False
            从dp[0][2]开始，当j位置字符为'*'时，dp[0][j-2]为真，dp[0][j]为真；
            其一不为真，则dp[0][j]都为False
    2. 按行更新dp，假设需要更新的位置为dp[i + 1][j + 1]：
        2.1 p[j] == '*'
            · 重复p[j-1] 0次，dp[i + 1][j + 1] = dp[i + 1][j - 2]
            · 重复p[j-1] 1次：
                dp[i][j + 1] == True，即p上新增一个字符正好匹配上了s的当前位置的字符
                p的上一个元素能与s的当前元素匹配：dp[j - 1] == s[i] or dp[j - 1] == '.'

    3. 返回dp[-1][-1]即可

    :param s:
    :param p:
    :return:
    """
    # 如果字符规律串为空，字符匹配串为空返回True，否则返回False
    if not p:
        return not s

    dp = [[False for j in range((len(p) + 1))] for i in range(len(s) + 1)]
    dp[0][0] = True
    # 更新dp第0行元素的值, dp[0][0] = True, dp[0][1] = False
    for j in range(2, len(p) + 1):
        # 从j = 2开始，当前元素为'*'时，还需往前看两个位置；其一不为真，则dp[0][j]就为False
        if p[j - 1] == '*' and dp[0][j - 2]:
            dp[0][j] = True

    # 按行更新dp
    for i in range(len(s)):
        for j in range(len(p)):
            # 当
            if p[j] == '*':
                dp[i + 1][j + 1] = dp[i + 1][j - 1] or (dp[i][j + 1] and (p[j - 1] == s[i] or p[j - 1] == '.'))
            else:
                dp[i + 1][j + 1] = dp[i][j] and (p[j] == s[i] or p[j] == '.')

    return dp[len(s)][len(p)]


# print(isMatch('aa', 'a'))
# print(isMatch('aa', 'a*'))
# print(isMatch('aa', 'a.'))
# print(isMatch('aab', 'c*a*b*'))
# print(isMatch("mississippi", "mis*is*p*."))
# print(isMatch("mississippi", "mis*is*ip*."))
# print(isMatch('ab', '.*c'))
# print(isMatch('ab', '.*'))
# print(isMatch1('ab', '.*'))
print(isMatch1('aab', 'c*a*b*'))
