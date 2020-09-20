from LeetCode.TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            # 保存右节点的信息
            right = root.right
            # 右节点递归翻转
            root.right = self.invertTree(root.left)
            # 左节点递归翻转
            root.left = self.invertTree(right)
            return root
        else:
            return None


Solution().invertTree(TreeNode(-1).list2Tree([1, 'null', 2])).print_tree()
