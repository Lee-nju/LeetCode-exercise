from LeetCode.TreeNode import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            # 小于当前节点的值，往左子树找
            if val < node.val:
                # 左子树不空，往左子树找
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
            # 大于当前节点的值，往右子树找
            else:
                # 右子树不空，往右子树找
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
        return root


root = TreeNode(-1).list2Tree([4, 2, 7, 1, 3])
Solution().insertIntoBST(root, 5).print_tree()
