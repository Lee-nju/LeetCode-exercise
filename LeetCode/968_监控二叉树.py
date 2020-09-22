from LeetCode.TreeNode import TreeNode

result = 0


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        global result
        if cameraCover(root) == 0:
            result += 1
        k, result = result, 0
        return k


def cameraCover(root: TreeNode) -> int:
    global result
    if not root:
        return 2

    left = cameraCover(root.left)
    right = cameraCover(root.right)

    if left == right == 2:
        return 0
    elif left == 0 or right == 0:
        result += 1
        return 1
    elif left == 1 or right == 1:
        return 2
