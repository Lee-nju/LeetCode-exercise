from collections import deque

from LeetCode.TreeNode import TreeNode


def inorderTraversal(root: TreeNode) -> [int]:
    res, stack = [], deque()
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.val)
            node = node.right

    return res


print(inorderTraversal(TreeNode(-1).list2Tree([1, 'null', 2, 3])))
