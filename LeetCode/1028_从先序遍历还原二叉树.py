from LeetCode.TreeNode import TreeNode
from collections import deque


def transform(S: str, index: int):
    """
    当前节点的值

    :param S:
    :param index:
    :return:
    """
    num = 0
    while index < len(S) and '0' <= S[index] <= '9':
        num = num * 10 + int(S[index])
        index += 1

    return num, index


def depth(S: str, index: int):
    """
    当前节点的深度

    :param S:
    :param index:
    :return:
    """
    dep = 0
    while index < len(S) and S[index] == '-':
        dep = dep + 1
        index = index + 1

    return dep, index


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        # 根节点的值
        val, begin = transform(S, 0)
        # 建树
        root = TreeNode(val)
        stack = deque()
        stack.append(root)
        # 循环至字符串结尾
        while begin < len(S):
            # 当前节点的深度，并更新下标
            dep, begin = depth(S, begin)
            # 当前节点的值，并更新下标
            val, begin = transform(S, begin)
            # 如果深度小于栈里的元素个数，出栈至深度等于栈里的元素个数
            if dep < len(stack):
                while dep < len(stack):
                    stack.pop()

                node = TreeNode(val)
                # 将其加到栈顶的右子节点上
                stack[-1].right = node
                # 入栈
                stack.append(node)

            # 如果深度等于栈里的元素个数
            else:
                # 临时节点加到栈顶的左子节点上，并入栈
                node = TreeNode(val)
                stack[-1].left = node
                stack.append(node)

        return stack[0]


Solution().recoverFromPreorder("1-2--3--4-5--6--7").print_tree()
Solution().recoverFromPreorder("1-2--3---4-5--6---7").print_tree()
