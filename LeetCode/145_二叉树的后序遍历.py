from LeetCode.TreeNode import TreeNode
from collections import deque


def postorderTraversal(root: TreeNode) -> [int]:
    res, stack = [], deque()
    node = root
    while node or stack:
        if node:
            stack.append([node, 0])
            node = node.left
        elif stack[-1][1] == 0:
            stack[-1][1] += 1
            node = stack[-1][0].right
        # 第二次遍历到节点时才出栈
        else:
            node = stack.pop()[0]
            res.append(node.val)
            node = None

    return res


print(postorderTraversal(TreeNode(-1).list2Tree([1, 'null', 2, 3])))
