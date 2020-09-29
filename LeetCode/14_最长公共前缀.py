class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            j, ch = 1, strs[0][i]
            while j < len(strs):
                # 如果第 j 个串的长度小于 i+1 或与所需要的串不相等，循环结束
                if len(strs[j]) - 1 < i or strs[j][i] != ch:
                    return res
                j += 1
            # 每个字符都相等，最长前缀加1
            res += ch

        return res


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["aa", "a"]))
