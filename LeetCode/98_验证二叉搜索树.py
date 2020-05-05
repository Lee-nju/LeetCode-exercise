from LeetCode.TreeNode import TreeNode


def isValidBST(root: TreeNode) -> bool:
    if not root:
        return True

    return inOrderTraverse([], root)


def inOrderTraverse(val, node: TreeNode) -> bool:
    if node.left:
        if not inOrderTraverse(val, node.left):
            return False

    if not val:
        val.append(node.val)
    elif val[0] < node.val:
        val[0] = node.val
    else:
        return False

    if node.right:
        if not inOrderTraverse(val, node.right):
            return False

    return True


# l = [5, 1, 4, 'null', 'null', 3, 6]
# tree = TreeNode(-1).list2Tree(l)
# print(isValidBST(tree))
#
# print(isValidBST(TreeNode(-1).list2Tree([0])))
# print(isValidBST(TreeNode(-1).list2Tree([0, -1, 'null'])))
# print(isValidBST(TreeNode(-1).list2Tree([2, 1, 3])))
# print(isValidBST(TreeNode(-1).list2Tree([1, 1])))
print(isValidBST(TreeNode(-1).list2Tree([0, 'null', -1])))
