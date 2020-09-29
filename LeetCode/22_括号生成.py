class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res, suf, pre = [], '(', '('

        def isParenthesis(suffix, tmp, leftBrace):
            """
            Solution:
                1. 当前累积子串长度为 2n 时，将其加入结果集合，结束
                2. 当前子串为空时，只能往里加入 '(' ，左括号个数加1
                3. 当前子串最后一个为 '(' 时，有两种选择
                    1. 继续加 '('，前提是左括号个数小于 n
                    2. 加 ')'，根据栈的设计，最后一个 '(' 出栈，累积子末尾加 ')'

            :param suffix: 前缀
            :param tmp: 当前的累积子串
            :param leftBrace: 有多少左括号
            :return:
            """
            if len(tmp) == 2 * n:
                res.append(tmp)
                return
            if suffix == '':
                suffix += '('
                tmp += '('
                isParenthesis(suffix, tmp, leftBrace + 1)
            elif suffix[-1] == '(':
                if leftBrace < n:
                    isParenthesis(suffix + '(', tmp + '(', leftBrace + 1)
                isParenthesis(suffix[:-1], tmp + ')', leftBrace)

        isParenthesis(suf, pre, 1)
        return res


print(*Solution().generateParenthesis(3), sep='\n')
