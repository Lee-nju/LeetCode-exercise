from LeetCode.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        # 当根节点的值在两个值之间时，根节点一定为两节点的最近公共祖先
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        # 当两个节点的值都比根节点值小时，递归到其左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 否则，两个节点的值肯定都比根节点值大，递归到其右子树
        else:
            return self.lowestCommonAncestor(root.right, p, q)


root = TreeNode(-1).list2Tree([6, 2, 8, 0, 4, 7, 9, 'null', 'null', 3, 5])
p = TreeNode(2)
q = TreeNode(4)

print(Solution().lowestCommonAncestor(root, p, q).val)
