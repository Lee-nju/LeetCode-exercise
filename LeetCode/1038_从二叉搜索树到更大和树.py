from LeetCode.TreeNode import TreeNode


def bstToGst(root: TreeNode) -> TreeNode:
    reverseInorderTrave(root, 0)
    return root


def reverseInorderTrave(root: TreeNode, sumOfRight):
    """
    利用递归来求解：
    在假设根有个右根节点下，从根出发开始递归，来更新根下面每个节点的值。

    :param root: 当前节点
    :param sumOfRight: 中序遍历时，当前节点右边所有点的和
    :return: 返回中序遍历时，上一节点之后所有点的和
    """
    # 如果是空节点，直接返回上一节点留下来的和
    if not root:
        return sumOfRight
    if root.right:
        root.val += reverseInorderTrave(root.right, sumOfRight)
    # 最右节点加上上一节点的值
    else:
        root.val += sumOfRight

    # 返回到其中序遍历的上一节点时，将值保留
    if root.left:
        return reverseInorderTrave(root.left, root.val)

    return root.val


# bstToGst(TreeNode(-1).list2Tree([5, 2, 13])).print_tree()
bstToGst(
    TreeNode(-1).list2Tree([4, 1, 6, 0, 2, 5, 7, 'null', 'null', 'null', 3, 'null', 'null', 'null', 8])).print_tree()
