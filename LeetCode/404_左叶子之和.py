from LeetCode.TreeNode import TreeNode


def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    res = 0
    # 如果左子树不空
    if root.left:
        # 看看左子树是不是叶子节点
        if root.left.left or root.left.right:
            res += sumOfLeftLeaves(root.left)
        # 如果左子树只有一个节点，将左子节点的值加上，结束
        else:
            res += root.left.val
    if root.right:
        res += sumOfLeftLeaves(root.right)

    return res


tree = TreeNode(-1).list2Tree([3, 9, 20, 'null', 'null', 15, 17])
print(sumOfLeftLeaves(tree))
