from LeetCode.TreeNode import TreeNode
from collections import deque


def transform(S: str, index: int):
    num = 0
    while index < len(S) and '0' <= S[index] <= '9':
        num = num * 10 + int(S[index])
        index += 1

    return num, index


def depth(S: str, index: int):
    dep = 0
    while index < len(S) and S[index] == '-':
        dep = dep + 1
        index = index + 1

    return dep, index


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        val, begin = transform(S, 0)
        root = TreeNode(val)
        stack = deque()
        stack.append(root)
        while begin < len(S):
            dep, begin = depth(S, begin)
            val, begin = transform(S, begin)
            if dep < len(stack):
                while dep < len(stack):
                    stack.pop()

                node = TreeNode(val)
                stack[-1].right = node
                stack.append(node)
            else:
                node = TreeNode(val)
                stack[-1].left = node
                stack.append(node)

        return stack[0]


Solution().recoverFromPreorder("1-2--3--4-5--6--7").print_tree()
Solution().recoverFromPreorder("1-2--3---4-5--6---7").print_tree()
