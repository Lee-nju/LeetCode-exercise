from LeetCode.TreeNode import TreeNode


def convertBST(root: TreeNode) -> TreeNode:
    """
    遍历顺序为：右->中->左
    或称为反中序遍历

    :param root:
    :return:
    """
    sumOfRight, stack = 0, []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.right
        else:
            node = stack.pop(-1)
            node.val += sumOfRight
            sumOfRight = node.val
            node = node.left

    return root


convertBST(TreeNode(-1).list2Tree([5, 2, 13])).print_tree()
