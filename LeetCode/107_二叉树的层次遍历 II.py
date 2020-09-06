from LeetCode.TreeNode import TreeNode
from collections import deque


def levelOrderBottom(root: TreeNode) -> [[int]]:
    if not root:
        return []
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        tmp = []
        k = len(queue)
        while k > 0:
            node = queue.popleft()
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            k = k - 1

        result.append(tmp)

    return result[::-1]


tree = TreeNode(-1).list2Tree([3, 9, 20, "null", "null", 15, 7])
print(levelOrderBottom(tree))
